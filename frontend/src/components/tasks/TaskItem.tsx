'use client';

import React, { useState, memo } from 'react';
import { Task } from '../../types/task'; // Changed from services/api to types/task
import { useApp } from '../../contexts/AppContext';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTag, faCalendarAlt, faExclamationCircle } from '@fortawesome/free-solid-svg-icons';


interface TaskItemProps {
  task: Task;
  onDelete: (id: string) => void;
  onToggle: (id: string) => void;
  onTaskSelect: (task: Task) => void; // New: Add onTaskSelect prop
}

const TaskItemComponent = ({ task, onDelete, onToggle, onTaskSelect }: TaskItemProps) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const editDescriptionInitial = task.description ?? '';
  const [editDescription, setEditDescription] = useState(editDescriptionInitial);
  const [editDueDate, setEditDueDate] = useState(task.dueDate ? new Date(task.dueDate).toISOString().split('T')[0] : '');
  const [editPriority, setEditPriority] = useState<'Low' | 'Medium' | 'High'>(task.priority || 'Medium');
  const [editTags, setEditTags] = useState<string[]>(task.tags || []);
  const [currentEditTagInput, setCurrentEditTagInput] = useState('');

  const [isUpdating, setIsUpdating] = useState(false);
  const [showConfirmDelete, setShowConfirmDelete] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);
  const [isToggling, setIsToggling] = useState(false); // New state for toggle loading

  const { updateTask } = useApp();

  const handleAddEditTag = () => {
    if (currentEditTagInput.trim() && !editTags.includes(currentEditTagInput.trim())) {
      setEditTags([...editTags, currentEditTagInput.trim()]);
      setCurrentEditTagInput('');
    }
  };

  const handleRemoveEditTag = (tagToRemove: string) => {
    setEditTags(editTags.filter(tag => tag !== tagToRemove));
  };


  const handleEdit = async () => {
    if (!editTitle.trim()) return;

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
      // Error updating task - error is handled by context
    } finally {
      setIsUpdating(false);
    }
  };

  const handleDeleteClick = () => {
    setShowConfirmDelete(true);
  };

  const confirmDelete = async () => {
    setIsDeleting(true);
    setShowConfirmDelete(false);
    try {
      await onDelete(task.id);
    } catch (error) {
      console.error("Error during task deletion:", error);
    } finally {
      // isDeleting will naturally reset as component unmounts or task list updates
    }
  };

  const handleToggle = async () => {
    setIsToggling(true);
    try {
      await onToggle(task.id);
    } catch (error) {
      console.error("Error during task toggle:", error);
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
    <div className="p-4" role="listitem">
      {isEditing ? (
        <div className="border rounded-lg p-4 bg-white shadow-sm" role="form" aria-label={`Editing task: ${task.title}`}>
          <label htmlFor="edit-title" className="sr-only">Task Title</label>
          <input
            id="edit-title"
            type="text"
            value={editTitle}
            onChange={(e) => setEditTitle(e.target.value)}
            className="w-full p-2 border rounded mb-2 text-gray-900"
            placeholder="Task title"
            aria-label="Edit task title"
            autoFocus
          />
          <label htmlFor="edit-description" className="sr-only">Task Description</label>
          <textarea
            id="edit-description"
            value={editDescription}
            onChange={(e) => setEditDescription(e.target.value)}
            className="w-full p-2 border rounded mb-2 text-gray-900"
            placeholder="Task description"
            rows={2}
            aria-label="Edit task description"
          />

          {/* Edit Due Date */}
          <div className="mb-2">
            <label htmlFor="edit-dueDate" className="block text-sm font-medium text-gray-700 mb-1">Due Date</label>
            <input
              type="date"
              id="edit-dueDate"
              value={editDueDate}
              onChange={(e) => setEditDueDate(e.target.value)}
              className="w-full p-2 border rounded text-gray-900"
            />
          </div>

          {/* Edit Priority */}
          <div className="mb-2">
            <label htmlFor="edit-priority" className="block text-sm font-medium text-gray-700 mb-1">Priority</label>
            <select
              id="edit-priority"
              value={editPriority}
              onChange={(e) => setEditPriority(e.target.value as 'Low' | 'Medium' | 'High')}
              className="w-full p-2 border rounded text-gray-900"
            >
              <option value="Low">Low</option>
              <option value="Medium">Medium</option>
              <option value="High">High</option>
            </select>
          </div>

          {/* Edit Tags */}
          <div className="mb-4">
            <label htmlFor="edit-tag-input" className="block text-sm font-medium text-gray-700 mb-1">Tags</label>
            <div className="flex items-center space-x-2 mb-2">
              <input
                type="text"
                id="edit-tag-input"
                value={currentEditTagInput}
                onChange={(e) => setCurrentEditTagInput(e.target.value)}
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    e.preventDefault();
                    handleAddEditTag();
                  }
                }}
                className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md p-2 text-gray-900"
                placeholder="Add a tag and press Enter"
              />
              <button
                type="button"
                onClick={handleAddEditTag}
                className="inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700"
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
                  >
                    <FontAwesomeIcon icon={faTimes} className="h-2 w-2" />
                  </button>
                </span>
              ))}
            </div>
          </div>


          <div className="flex flex-col sm:flex-row justify-end space-y-2 sm:space-y-0 sm:space-x-2">
            <button
              onClick={() => setIsEditing(false)}
              className="px-3 py-1 text-sm bg-gray-200 rounded hover:bg-gray-300 sm:w-auto"
              disabled={isUpdating}
              aria-label="Cancel editing"
            >
              Cancel
            </button>
            <button
              onClick={handleEdit}
              className="px-3 py-1 text-sm bg-indigo-600 text-white rounded hover:bg-indigo-700 sm:w-auto"
              disabled={isUpdating}
              aria-label="Save changes"
            >
              {isUpdating ? 'Saving...' : 'Save'}
            </button>
          </div>
        </div>
      ) : (
        <div className={`border rounded-lg p-4 shadow-sm transition-all duration-200 ${task.completed ? 'bg-gray-50' : 'bg-white hover:shadow-md'}`}>
          <div className="flex items-start justify-between flex-wrap gap-2">
            <div className="flex-1 min-w-0">
              <div className="flex items-start mb-1">
                {isToggling ? (
                  <div className="h-5 w-5 flex items-center justify-center">
                    <svg className="animate-spin h-4 w-4 text-indigo-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                  </div>
                ) : (
                  <input
                    type="checkbox"
                    checked={task.completed}
                    onChange={handleToggle}
                    className="h-5 w-5 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500 mt-0.5 cursor-pointer flex-shrink-0"
                    id={`task-checkbox-${task.id}`}
                    aria-label={task.completed ? `Mark task "${task.title}" as incomplete` : `Mark task "${task.title}" as complete`}
                    disabled={isToggling} // Disable while toggling
                  />
                )}
                <div
                  className="flex-1 ml-3 cursor-pointer" // This div becomes clickable
                  onClick={() => onTaskSelect(task)}
                >
                  <label
                    htmlFor={`task-checkbox-${task.id}`}
                    className={`text-lg font-semibold block ${
                      task.completed ? 'text-gray-500 line-through' : 'text-gray-900'
                    }`}
                  >
                    {task.title}
                  </label>
                  {task.description && (
                    <p className="text-sm text-gray-600 mt-1" aria-label={`Description: ${task.description}`}>{task.description}</p>
                  )}
                  
                  <div className="mt-2 flex flex-wrap items-center gap-x-4 gap-y-2 text-sm text-gray-600">
                    {task.dueDate && (
                      <span className="flex items-center">
                        <FontAwesomeIcon icon={faCalendarAlt} className="mr-1 text-gray-400" />
                        Due: {new Date(task.dueDate).toLocaleDateString()}
                      </span>
                    )}
                    {task.priority && (
                      <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${getPriorityClass(task.priority)}`}>
                        <FontAwesomeIcon icon={faExclamationCircle} className="mr-1" />
                        {task.priority}
                      </span>
                    )}
                    {task.tags && task.tags.length > 0 && (
                      <div className="flex flex-wrap gap-1">
                        {task.tags.map((tag, index) => (
                          <span key={index} className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                            <FontAwesomeIcon icon={faTag} className="mr-1" />
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                  <span className="text-xs text-gray-500 mt-2 block" aria-label={`Created on ${new Date(task.created_at).toLocaleDateString()}`}>
                    Created: {new Date(task.created_at).toLocaleDateString()}
                  </span>
                  {new Date(task.created_at).getTime() !== new Date(task.updated_at).getTime() && (
                    <span className="text-xs text-gray-500 mt-1 block" aria-label={`Last updated on ${new Date(task.updated_at).toLocaleDateString()}`}>
                      Updated: {new Date(task.updated_at).toLocaleDateString()}
                    </span>
                  )}
                </div>
              </div>
            </div>
            <div className="flex space-x-2 flex-shrink-0 mt-2 sm:mt-0">
              <button
                onClick={() => setIsEditing(true)}
                className="text-blue-600 hover:text-blue-800 p-1 rounded hover:bg-blue-50"
                aria-label={`Edit task "${task.title}"`}
                disabled={isDeleting || isToggling} // Disable edit while deleting or toggling
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-5 w-5"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                  aria-hidden="true"
                >
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                </svg>
              </button>
              <button
                onClick={handleDeleteClick}
                className="text-red-600 hover:text-red-800 p-1 rounded hover:bg-red-50"
                aria-label={`Delete task "${task.title}"`}
                disabled={isDeleting || isToggling} // Disable delete while deleting or toggling
              >
                {isDeleting ? (
                  <svg className="animate-spin h-5 w-5 text-red-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                ) : (
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fillRule="evenodd"
                      d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                      clipRule="evenodd"
                    />
                  </svg>
                )}
              </button>
            </div>
          </div>

          {/* Confirmation Modal */}
          {showConfirmDelete && (
            <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex justify-center items-center z-50">
              <div className="bg-white p-6 rounded-lg shadow-xl max-w-sm mx-auto">
                <h3 className="text-lg font-semibold text-gray-900 mb-4">Confirm Deletion</h3>
                <p className="text-sm text-gray-600 mb-6">Are you sure you want to delete the task &quot;{task.title}&quot;? This action cannot be undone.</p>
                <div className="flex justify-end space-x-3">
                  <button
                    onClick={() => setShowConfirmDelete(false)}
                    className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
                    disabled={isDeleting || isToggling} // Disable cancel while deleting or toggling
                  >
                    Cancel
                  </button>
                  <button
                    onClick={confirmDelete}
                    className="px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                    disabled={isDeleting || isToggling} // Disable confirm while deleting or toggling
                  >
                    {isDeleting ? 'Deleting...' : 'Delete'}
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export const TaskItem = memo(TaskItemComponent, (prevProps, nextProps) =>
  prevProps.task.id === nextProps.task.id &&
  prevProps.task.title === nextProps.task.title &&
  prevProps.task.description === nextProps.task.description &&
  prevProps.task.completed === nextProps.task.completed &&
  prevProps.task.created_at === nextProps.task.created_at &&
  prevProps.task.updated_at === nextProps.task.updated_at &&
  prevProps.task.dueDate === nextProps.task.dueDate &&
  prevProps.task.priority === nextProps.task.priority &&
  JSON.stringify(prevProps.task.tags) === JSON.stringify(nextProps.task.tags)
);