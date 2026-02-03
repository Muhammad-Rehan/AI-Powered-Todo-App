import React, { useState, memo } from 'react';
import { Task } from '../../types/task';
import { useApp } from '../../contexts/AppContext'; // Import useApp
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes, faCalendarAlt, faExclamationCircle, faTag, faCheckCircle, faCircle, faEdit, faSave, faTrashAlt, faUndo, faSquare, faCheckSquare } from '@fortawesome/free-solid-svg-icons'; // Added faSquare, faCheckSquare

interface TaskDetailProps {
  task: Task;
  onClose: () => void;
}

const TaskDetail: React.FC<TaskDetailProps> = ({ task, onClose }) => {
  const { updateTask, deleteTask, toggleTaskCompletion } = useApp(); // Get toggleTaskCompletion from context

  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const editDescriptionInitial = task.description ?? '';
  const [editDescription, setEditDescription] = useState(editDescriptionInitial);
  const [editDueDate, setEditDueDate] = useState(task.dueDate ? new Date(task.dueDate).toISOString().split('T')[0] : '');
  const [editPriority, setEditPriority] = useState<'Low' | 'Medium' | 'High'>(task.priority || 'Medium');
  const [editTags, setEditTags] = useState<string[]>(task.tags || []);
  const [currentEditTagInput, setCurrentEditTagInput] = useState('');

  const [isUpdating, setIsUpdating] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);
  const [isToggling, setIsToggling] = useState(false); // New state for toggle loading
  const [showConfirmDelete, setShowConfirmDelete] = useState(false);


  const handleAddEditTag = () => {
    if (currentEditTagInput.trim() && !editTags.includes(currentEditTagInput.trim())) {
      setEditTags([...editTags, currentEditTagInput.trim()]);
      setCurrentEditTagInput('');
    }
  };

  const handleRemoveEditTag = (tagToRemove: string) => {
    setEditTags(editTags.filter(tag => tag !== tagToRemove));
  };

  const handleEditClick = () => {
    setIsEditing(true);
    // Initialize edit states with current task values
    setEditTitle(task.title);
    setEditDescription(task.description ?? '');
    setEditDueDate(task.dueDate ? new Date(task.dueDate).toISOString().split('T')[0] : '');
    setEditPriority(task.priority || 'Medium');
    setEditTags(task.tags || []);
    setCurrentEditTagInput('');
  };

  const handleCancelEdit = () => {
    setIsEditing(false);
    // Reset states to original task values
    setEditTitle(task.title);
    setEditDescription(task.description ?? '');
    setEditDueDate(task.dueDate ? new Date(task.dueDate).toISOString().split('T')[0] : '');
    setEditPriority(task.priority || 'Medium');
    setEditTags(task.tags || []);
    setCurrentEditTagInput('');
  };

  const handleSaveEdit = async () => {
    if (!editTitle.trim()) {
      alert('Title cannot be empty');
      return;
    }
    setIsUpdating(true);
    try {
      await updateTask(task.id, {
        title: editTitle,
        description: editDescription,
        dueDate: editDueDate || undefined,
        priority: editPriority,
        tags: editTags.length > 0 ? editTags : undefined,
      });
      setIsEditing(false);
    } catch (error) {
    } finally {
      setIsUpdating(false);
    }
  };

  const handleDeleteClick = () => {
    setShowConfirmDelete(true);
  };

  const confirmDelete = async () => {
    setIsDeleting(true);
    try {
      await deleteTask(task.id);
      onClose(); // Close the detail panel after deletion
    } catch (error) {
    } finally {
      setIsDeleting(false);
    }
  };

  const handleToggleCompletion = async () => {
    setIsToggling(true);
    try {
      await toggleTaskCompletion(task.id);
      // The task list will refetch, so the task prop should update naturally
    } catch (error) {
    } finally {
      setIsToggling(false);
    }
  };


  const getPriorityClass = (priority: 'Low' | 'Medium' | 'High' | undefined) => {
    switch (priority) {
      case 'Low':
        return 'bg-green-100 text-green-800';
      case 'Medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'High':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="fixed top-0 right-0 w-96 h-full bg-white shadow-2xl flex flex-col z-50 overflow-y-auto">
      <header className="bg-indigo-600 text-white p-4 flex justify-between items-center">
        <h2 className="text-xl font-bold">{isEditing ? 'Edit Task' : 'Task Details'}</h2>
        <div className="flex items-center space-x-2">
          {!isEditing && (
            <button
              onClick={handleEditClick}
              className="p-1 rounded-full hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-white"
              aria-label="Edit task"
              disabled={isUpdating || isDeleting || isToggling}
            >
              <FontAwesomeIcon icon={faEdit} className="h-5 w-5" />
            </button>
          )}
          <button
            onClick={onClose}
            className="p-1 rounded-full hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-white"
            aria-label="Close task details"
            disabled={isUpdating || isDeleting || isToggling}
          >
            <FontAwesomeIcon icon={faTimes} className="h-5 w-5" />
          </button>
        </div>
      </header>

      <div className="p-4 flex-grow">
        {isEditing ? (
          <div className="space-y-4">
            <div>
              <label htmlFor="edit-detail-title" className="block text-sm font-medium text-gray-700 mb-1">Title *</label>
              <input
                id="edit-detail-title"
                type="text"
                value={editTitle}
                onChange={(e) => setEditTitle(e.target.value)}
                className="w-full p-2 border rounded text-gray-900"
                aria-label="Edit task title"
              />
            </div>
            <div>
              <label htmlFor="edit-detail-description" className="block text-sm font-medium text-gray-700 mb-1">Description</label>
              <textarea
                id="edit-detail-description"
                value={editDescription}
                onChange={(e) => setEditDescription(e.target.value)}
                rows={3}
                className="w-full p-2 border rounded text-gray-900"
                aria-label="Edit task description"
              />
            </div>
            <div>
              <label htmlFor="edit-detail-dueDate" className="block text-sm font-medium text-gray-700 mb-1">Due Date</label>
              <input
                id="edit-detail-dueDate"
                type="date"
                value={editDueDate}
                onChange={(e) => setEditDueDate(e.target.value)}
                className="w-full p-2 border rounded text-gray-900"
                aria-label="Edit task due date"
              />
            </div>
            <div>
              <label htmlFor="edit-detail-priority" className="block text-sm font-medium text-gray-700 mb-1">Priority</label>
              <select
                id="edit-detail-priority"
                value={editPriority}
                onChange={(e) => setEditPriority(e.target.value as 'Low' | 'Medium' | 'High')}
                className="w-full p-2 border rounded text-gray-900"
                aria-label="Edit task priority"
              >
                <option value="Low">Low</option>
                <option value="Medium">Medium</option>
                <option value="High">High</option>
              </select>
            </div>
            <div>
              <label htmlFor="edit-detail-tag-input" className="block text-sm font-medium text-gray-700 mb-1">Tags</label>
              <div className="flex items-center space-x-2 mb-2">
                <input
                  id="edit-detail-tag-input"
                  type="text"
                  value={currentEditTagInput}
                  onChange={(e) => setCurrentEditTagInput(e.target.value)}
                  onKeyPress={(e) => {
                    if (e.key === 'Enter') {
                      e.preventDefault();
                      handleAddEditTag();
                    }
                  }}
                  className="w-full p-2 border rounded text-gray-900"
                  placeholder="Add a tag and press Enter"
                  aria-label="Add new tags"
                />
                <button
                  type="button"
                  onClick={handleAddEditTag}
                  className="px-3 py-1.5 bg-indigo-600 text-white rounded-md text-sm hover:bg-indigo-700"
                >
                  Add
                </button>
              </div>
              <div className="flex flex-wrap gap-2">
                {editTags.map((tag, index) => (
                  <span
                    key={index}
                    className="inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800"
                  >
                    {tag}
                    <button
                      type="button"
                      onClick={() => handleRemoveEditTag(tag)}
                      className="ml-1 -mr-0.5 h-4 w-4 rounded-full flex items-center justify-center text-indigo-600 hover:bg-indigo-200"
                      aria-label={`Remove tag ${tag}`}
                    >
                      <FontAwesomeIcon icon={faTimes} className="h-2 w-2" />
                    </button>
                  </span>
                ))}
              </div>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            <h3 className="text-2xl font-bold text-gray-900 mb-2">{task.title}</h3>
            {task.description && (
              <p className="text-gray-700">{task.description}</p>
            )}

            <div className="space-y-3 pt-2">
              <p className="text-sm text-gray-600 flex items-center">
                {task.completed ? (
                  <FontAwesomeIcon icon={faCheckCircle} className="mr-2 text-green-500" />
                ) : (
                  <FontAwesomeIcon icon={faCircle} className="mr-2 text-yellow-500" />
                )}
                Status: {task.completed ? 'Completed' : 'Active'}
              </p>
              {task.dueDate && (
                <p className="text-sm text-gray-600 flex items-center">
                  <FontAwesomeIcon icon={faCalendarAlt} className="mr-2 text-gray-500" />
                  Due Date: {new Date(task.dueDate).toLocaleDateString()}
                </p>
              )}
              {task.priority && (
                <p className="text-sm text-gray-600 flex items-center">
                  <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${getPriorityClass(task.priority)}`}>
                    <FontAwesomeIcon icon={faExclamationCircle} className="mr-2" />
                    Priority: {task.priority}
                  </span>
                </p>
              )}
              <p className="text-sm text-gray-600 flex items-center">
                Created: {new Date(task.created_at).toLocaleDateString()}
              </p>
              {new Date(task.created_at).getTime() !== new Date(task.updated_at).getTime() && (
                <p className="text-sm text-gray-600 flex items-center">
                  Updated: {new Date(task.updated_at).toLocaleDateString()}
                </p>
              )}
            </div>

            {task.tags && task.tags.length > 0 && (
              <div className="pt-2">
                <h4 className="text-md font-semibold text-gray-800 mb-2">Tags:</h4>
                <div className="flex flex-wrap gap-2">
                  {task.tags.map((tag, index) => (
                    <span key={index} className="inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
                      <FontAwesomeIcon icon={faTag} className="mr-1" />
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      <footer className="p-4 border-t border-gray-200 flex justify-between space-x-2">
        {isEditing ? (
          <>
            <button
              onClick={handleCancelEdit}
              className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 flex-1"
              disabled={isUpdating}
            >
              <FontAwesomeIcon icon={faUndo} className="mr-2" /> Cancel
            </button>
            <button
              onClick={handleSaveEdit}
              className="px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 flex-1"
              disabled={isUpdating}
            >
              {isUpdating ? 'Saving...' : <><FontAwesomeIcon icon={faSave} className="mr-2" /> Save</>}
            </button>
          </>
        ) : (
          <>
            <button
              onClick={handleDeleteClick}
              className="px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 flex-1"
              disabled={isDeleting}
            >
              {isDeleting ? 'Deleting...' : <><FontAwesomeIcon icon={faTrashAlt} className="mr-2" /> Delete</>}
            </button>
            <button
              onClick={handleEditClick}
              className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 flex-1"
              disabled={isUpdating || isDeleting}
            >
              <FontAwesomeIcon icon={faEdit} className="mr-2" /> Edit
            </button>
            <button
              onClick={handleToggleCompletion}
              className={`px-4 py-2 text-sm font-medium text-white rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 flex-1
                ${task.completed ? 'bg-yellow-500 hover:bg-yellow-600 focus:ring-yellow-500' : 'bg-green-600 hover:bg-green-700 focus:ring-green-500'}`}
              disabled={isUpdating || isDeleting || isToggling}
            >
              {isToggling ? (
                <FontAwesomeIcon icon={faCircle} className="mr-2 animate-pulse" />
              ) : task.completed ? (
                <FontAwesomeIcon icon={faSquare} className="mr-2" />
              ) : (
                <FontAwesomeIcon icon={faCheckSquare} className="mr-2" />
              )}
              {task.completed ? 'Mark Active' : 'Mark Completed'}
            </button>
          </>
        )}
      </footer>

      {/* Confirmation Modal */}
      {showConfirmDelete && (
        <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex justify-center items-center z-50">
          <div className="bg-white p-6 rounded-lg shadow-xl max-w-sm mx-auto">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Confirm Deletion</h3>
            <p className="text-sm text-gray-600 mb-6">Are you sure you want to delete &quot;{task.title}&quot;? This action cannot be undone.</p>
            <div className="flex justify-end space-x-3">
              <button
                onClick={() => setShowConfirmDelete(false)}
                className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
                disabled={isDeleting}
              >
                Cancel
              </button>
              <button
                onClick={confirmDelete}
                className="px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                disabled={isDeleting}
              >
                {isDeleting ? 'Deleting...' : 'Delete'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskDetail;
