export interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
  dueDate?: string; // New: Optional due date
  priority?: 'Low' | 'Medium' | 'High'; // New: Optional priority
  tags?: string[]; // New: Optional array of tags
}

export interface CreateTaskData {
  title: string;
  description?: string;
  completed: boolean;
  dueDate?: string;
  priority?: 'Low' | 'Medium' | 'High';
  tags?: string[];
}

export interface UpdateTaskData {
  title?: string;
  description?: string;
  completed?: boolean;
  dueDate?: string;
  priority?: 'Low' | 'Medium' | 'High';
  tags?: string[];
}