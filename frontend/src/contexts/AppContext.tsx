'use client';

import React, {
  createContext,
  useContext,
  useReducer,
  ReactNode,
  useEffect,
} from 'react';
import { Task } from '../types/task';
import { apiService } from '../services/api';

/* =======================
   Types
======================= */

interface User {
  user_id: string;
  email: string;
}

interface LoadingState {
  auth: boolean;
  tasks: boolean;
}

interface AppState {
  user: User | null;
  token: string | null;
  tasks: Task[];
  loadingState: LoadingState;
  error: string | null;
  notification: { message: string; type: 'success' | 'error'; visible: boolean } | null; // Added notification state
}

type AppAction =
  | { type: 'SET_USER'; payload: { user: User; token: string } }
  | { type: 'LOGOUT' }
  | { type: 'SET_TASKS'; payload: Task[] }
  | { type: 'ADD_TASK'; payload: Task }
  | { type: 'UPDATE_TASK'; payload: Task }
  | { type: 'DELETE_TASK'; payload: string }
  | { type: 'SET_LOADING'; payload: { section: keyof LoadingState; value: boolean } }
  | { type: 'SET_ERROR'; payload: string | null }
  | { type: 'SET_NOTIFICATION'; payload: { message: string; type: 'success' | 'error' } | null }; // New action for notifications

/* =======================
   Initial State
======================= */

const initialState: AppState = {
  user: null,
  token: null,
  tasks: [],
  loadingState: {
    auth: false,
    tasks: false,
  },
  error: null,
  notification: null, // Initialized notification state
};

/* =======================
   Reducer
======================= */

const appReducer = (state: AppState, action: AppAction): AppState => {
  switch (action.type) {
    case 'SET_USER':
      return {
        ...state,
        user: action.payload.user,
        token: action.payload.token,
        error: null,
      };

    case 'LOGOUT':
      return { ...initialState };

    case 'SET_TASKS':
      return {
        ...state,
        tasks: action.payload,
        loadingState: { ...state.loadingState, tasks: false },
      };

    case 'ADD_TASK':
      return { ...state, tasks: [...state.tasks, action.payload] };

    case 'UPDATE_TASK':
      return {
        ...state,
        tasks: state.tasks.map(task =>
          task.id === action.payload.id ? action.payload : task
        ),
      };

    case 'DELETE_TASK':
      return {
        ...state,
        tasks: state.tasks.filter(task => task.id !== action.payload),
      };

    case 'SET_LOADING':
      return {
        ...state,
        loadingState: {
          ...state.loadingState,
          [action.payload.section]: action.payload.value,
        },
      };

    case 'SET_ERROR':
      return {
        ...state,
        error: action.payload,
        loadingState: { auth: false, tasks: false },
      };

    case 'SET_NOTIFICATION':
      return {
        ...state,
        notification: action.payload ? { ...action.payload, visible: true } : null,
      };


    default:
      return state;
  }
};

/* =======================
   Context
======================= */

interface AppContextType extends AppState {
  signIn: (email: string, password: string) => Promise<any>;
  signUp: (email: string, password: string) => Promise<any>;
  signOut: () => void;
  fetchTasks: () => Promise<void>;
  createTask: (taskData: Omit<Task, 'id' | 'user_id' | 'created_at'>) => Promise<void>;
  updateTask: (id: string, taskData: Partial<Task>) => Promise<void>;
  deleteTask: (id: string) => Promise<void>;
  toggleTaskCompletion: (id: string) => Promise<void>;
  refetchTasks: () => Promise<void>;
  showNotification: (message: string, type: 'success' | 'error') => void;
  removeTaskFromState: (id: string) => void; // New: function to remove task from local state
}

const AppContext = createContext<AppContextType | undefined>(undefined);

/* =======================
   Provider
======================= */

export const AppProvider = ({ children }: { children: ReactNode }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  // New: Timeout ref for notifications
  const notificationTimeoutRef = React.useRef<NodeJS.Timeout | null>(null);

  /* Restore auth on load */
  useEffect(() => {
    const token = localStorage.getItem('token');
    const user = localStorage.getItem('user');

    if (token && user) {
      try {
        dispatch({
          type: 'SET_USER',
          payload: { token, user: JSON.parse(user) },
        });
      } catch {
        localStorage.clear();
      }
    }
  }, []);

  // New: Effect to clear notification timeout on unmount or new notification
  useEffect(() => {
    return () => {
      if (notificationTimeoutRef.current) {
        clearTimeout(notificationTimeoutRef.current);
      }
    };
  }, []);

  /* =======================
     Notification Actions
  ======================= */
  const showNotification = (message: string, type: 'success' | 'error') => {
    if (notificationTimeoutRef.current) {
      clearTimeout(notificationTimeoutRef.current);
    }

    dispatch({ type: 'SET_NOTIFICATION', payload: { message, type } });

    notificationTimeoutRef.current = setTimeout(() => {
      dispatch({ type: 'SET_NOTIFICATION', payload: null });
    }, 3000); // Hide after 3 seconds
  };


  /* =======================
     Auth Actions
  ======================= */

  const signIn = async (email: string, password: string) => {
    dispatch({ type: 'SET_LOADING', payload: { section: 'auth', value: true } });
    try {
      const data = await apiService.signIn(email, password);

      localStorage.setItem('token', data.token);
      localStorage.setItem(
        'user',
        JSON.stringify({ user_id: data.user_id, email: data.email })
      );

      dispatch({
        type: 'SET_USER',
        payload: {
          token: data.token,
          user: { user_id: data.user_id, email: data.email },
        },
      });

      return data;
    } catch (err: any) {
      dispatch({ type: 'SET_ERROR', payload: err.message });
      throw err;
    } finally {
      dispatch({ type: 'SET_LOADING', payload: { section: 'auth', value: false } });
    }
  };

  const signUp = async (email: string, password: string) => {
    dispatch({ type: 'SET_LOADING', payload: { section: 'auth', value: true } });
    try {
      const data = await apiService.signUp(email, password);

      localStorage.setItem('token', data.token);
      localStorage.setItem(
        'user',
        JSON.stringify({ user_id: data.user_id, email: data.email })
      );

      dispatch({
        type: 'SET_USER',
        payload: {
          token: data.token,
          user: { user_id: data.user_id, email: data.email },
        },
      });

      return data;
    } catch (err: any) {
      dispatch({ type: 'SET_ERROR', payload: err.message });
      throw err;
    } finally {
      dispatch({ type: 'SET_LOADING', payload: { section: 'auth', value: false } });
    }
  };

  const signOut = () => {
    localStorage.clear();
    dispatch({ type: 'LOGOUT' });
  };

  /* =======================
     Task Actions
  ======================= */

  const fetchTasks = async () => {
    if (!state.token) return;

    dispatch({ type: 'SET_LOADING', payload: { section: 'tasks', value: true } });
    try {
      const tasks = await apiService.getTasks(state.token);
      console.log("fetchTasks: tasks received:", tasks); // DEBUG LOG
      dispatch({ type: 'SET_TASKS', payload: tasks });
    } catch (err: any) {
      console.error("fetchTasks: error received:", err); // DEBUG LOG
      dispatch({ type: 'SET_ERROR', payload: err.message });
    }
  };

  const createTask = async (taskData: any) => {
    if (!state.token) return;
    dispatch({ type: 'SET_LOADING', payload: { section: 'tasks', value: true } }); // Set loading to true
    try {
      const task = await apiService.createTask(taskData, state.token);
      dispatch({ type: 'ADD_TASK', payload: task });
      showNotification('Task created successfully!', 'success'); // Show success notification
    } catch (err: any) {
      dispatch({ type: 'SET_ERROR', payload: err.message });
      showNotification('Failed to create task.', 'error'); // Show error notification
      throw err; // Re-throw to allow TaskForm to catch if needed
    } finally {
      dispatch({ type: 'SET_LOADING', payload: { section: 'tasks', value: false } }); // Set loading to false
    }
  };

  const updateTask = async (id: string, taskData: Partial<Task>) => {
    if (!state.token) return;
    try {
      const task = await apiService.updateTask(id, taskData, state.token);
      dispatch({ type: 'UPDATE_TASK', payload: task });
      showNotification('Task updated successfully!', 'success');
    } catch (err: any) {
      dispatch({ type: 'SET_ERROR', payload: err.message });
      showNotification('Failed to update task.', 'error');
    }
  };

  const deleteTask = async (id: string) => {
    if (!state.token) return;
    try {
      await apiService.deleteTask(id, state.token);
      dispatch({ type: 'DELETE_TASK', payload: id });
      showNotification('Task deleted successfully!', 'success'); // Show success notification
    } catch (err: any) {
      dispatch({ type: 'SET_ERROR', payload: err.message });
      showNotification('Failed to delete task.', 'error'); // Show error notification
    }
  };

  const removeTaskFromState = (id: string) => {
    dispatch({ type: 'DELETE_TASK', payload: id });
    showNotification('Task removed from list.', 'success');
  };

  const toggleTaskCompletion = async (id: string) => {
    if (!state.token) return;
    try {
      const task = await apiService.toggleTaskCompletion(id, state.token);
      dispatch({ type: 'UPDATE_TASK', payload: task });
      showNotification(`Task marked as ${task.completed ? 'completed' : 'incomplete'}!`, 'success');
    } catch (err: any) {
      dispatch({ type: 'SET_ERROR', payload: err.message });
      showNotification('Failed to update task completion status.', 'error');
    }
  };

  return (
    <AppContext.Provider
      value={{
        ...state,
        signIn,
        signUp,
        signOut,
        fetchTasks,
        createTask,
        updateTask,
        deleteTask,
        toggleTaskCompletion,
        refetchTasks: fetchTasks,
        showNotification, // Provide showNotification through context
        removeTaskFromState, // Provide removeTaskFromState through context
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
/* =======================
   Hook
======================= */

export const useApp = () => {
  const ctx = useContext(AppContext);
  if (!ctx) throw new Error('useApp must be used inside AppProvider');
  return ctx;
};
