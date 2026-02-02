'use client';

import { useState, useEffect, useMemo } from 'react'; // Added useMemo
import { useRouter } from 'next/navigation';
import { useApp } from '../../contexts/AppContext';
import { TaskForm } from '../../components/tasks/TaskForm';
import { TaskList } from '../../components/tasks/TaskList';
import ChatBubble from '../../components/chat/ChatBubble';
import ChatWindow from '../../components/chat/ChatWindow';
import Sidebar from '../../components/Sidebar'; // Import the new Sidebar component
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import { Task } from '../../types/task'; // Import Task type
import TaskDetail from '../../components/tasks/TaskDetail'; // Import TaskDetail component

// Helper function to check if a date is today
const isToday = (dateString: string) => {
  const today = new Date();
  const date = new Date(dateString);
  return date.getDate() === today.getDate() &&
         date.getMonth() === today.getMonth() &&
         date.getFullYear() === today.getFullYear();
};

const DashboardPage = () => {
  const router = useRouter();
  const { user, loadingState, signOut, refetchTasks, removeTaskFromState, tasks } = useApp(); // Destructure tasks from useApp
  const [showForm, setShowForm] = useState(false);
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); // State for sidebar visibility
  const [selectedTask, setSelectedTask] = useState<Task | null>(null); // State for selected task
  const [showTodayTasksOnly, setShowTodayTasksOnly] = useState(false); // New state for today's tasks filter

  // Calculate today's tasks count
  const todayTasksCount = useMemo(() => {
    return tasks.filter(task => task.dueDate && isToday(task.dueDate) && !task.completed).length;
  }, [tasks]);

  // Redirect if user is not authenticated
  useEffect(() => {
    if (!loadingState.auth && !user) {
      router.push('/');
    }
  }, [user, loadingState.auth, router]);

  const handleSignOut = () => {
    signOut();
    router.push('/');
  };

  const toggleChat = () => {
    // Close task detail if chat is opened
    if (!isChatOpen) setSelectedTask(null);
    setIsChatOpen(!isChatOpen);
  };

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  const handleTaskSelect = (task: Task) => {
    // Close chat if task detail is opened
    if (selectedTask?.id !== task.id) setIsChatOpen(false);
    setSelectedTask(task);
  };

  const handleTaskDetailClose = () => {
    setSelectedTask(null);
  };

  const handleToggleShowTodayTasksOnly = () => {
    setShowTodayTasksOnly(prev => !prev);
  };

  // Show loading while auth state is being determined
  if (loadingState.auth || !user) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading...
      </div>
    );
  }

  return (
    <div className="flex min-h-screen bg-gray-50 overflow-hidden"> {/* Use flex for main layout, add overflow-hidden */}
      <Sidebar 
        isOpen={isSidebarOpen} 
        onClose={toggleSidebar} 
        todayTasksCount={todayTasksCount} // Pass to Sidebar
        showTodayTasksOnly={showTodayTasksOnly} // Pass to Sidebar
        onToggleShowTodayTasksOnly={handleToggleShowTodayTasksOnly} // Pass to Sidebar
      />

      <div className="flex-1 flex flex-col"> {/* Main content area */}
        <header className="bg-white shadow">
          <div className="px-4 py-6 sm:px-6 lg:px-8">
            <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4">
              <div className="flex items-center">
                <button
                  onClick={toggleSidebar}
                  className="lg:hidden mr-4 text-gray-600 hover:text-gray-900 focus:outline-none"
                  aria-label="Open sidebar"
                >
                  <FontAwesomeIcon icon={faBars} size="lg" />
                </button>
                <h1 className="text-2xl sm:text-3xl font-bold text-gray-900">Todo Dashboard</h1>
              </div>
              <div className="flex items-center justify-between w-full sm:w-auto gap-2 sm:gap-4">
                <span className="text-gray-700 text-sm sm:text-base">
                  Welcome, {user.email.split('@')[0]}
                </span>

                <button
                  onClick={() => setShowForm(!showForm)}
                  className="sm:hidden bg-indigo-600 text-white px-3 py-1.5 rounded-md text-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                >
                  {showForm ? 'Cancel' : '+'}
                </button>
                <button
                  onClick={handleSignOut}
                  className="bg-red-600 text-white px-3 py-1.5 rounded-md text-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 whitespace-nowrap"
                >
                  Logout
                </button>
              </div>
            </div>
          </div>
        </header>

        <main className={`flex-1 overflow-y-auto ${(isChatOpen || selectedTask) ? 'lg:mr-96' : ''}`}> {/* Apply conditional margin-right here for chat or task detail */}
          <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8"> {/* New wrapper for content alignment */}
            <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center mb-6 gap-4">
              <h2 className="text-xl sm:text-2xl font-semibold text-gray-800">Your Tasks</h2>
              <div className="flex gap-2">
                <button
                  onClick={() => router.push('/chat')}
                  className="hidden sm:block bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
                >
                  AI Chat Assistant
                </button>
                <button
                  onClick={() => setShowForm(!showForm)}
                  className="hidden sm:block bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                >
                  {showForm ? 'Cancel' : 'Add New Task'}
                </button>
              </div>
            </div>

            {showForm && (
              <div className="mb-6">
                <TaskForm onClose={() => setShowForm(false)} />
              </div>
            )}

            <TaskList 
              isChatOpen={isChatOpen || !!selectedTask} 
              onTaskSelect={handleTaskSelect} 
              showTodayTasksOnly={showTodayTasksOnly} // Pass new prop
            />
          </div>
        </main>
      </div>

      <ChatBubble onClick={toggleChat} />
      {isChatOpen && user && (
        <ChatWindow
          userId={user.user_id}
          onClose={toggleChat}
          onTaskAdded={refetchTasks}
          onTaskRemovedFromState={removeTaskFromState}
        />
      )}

      {selectedTask && (
        <TaskDetail task={selectedTask} onClose={handleTaskDetailClose} />
      )}
    </div>
  );
};

export default DashboardPage;
