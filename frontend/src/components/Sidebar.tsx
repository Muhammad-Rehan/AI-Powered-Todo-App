
'use client';

import React from 'react';
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch, faTimes, faCog, faPlus } from '@fortawesome/free-solid-svg-icons';
import clsx from 'clsx'; // Import clsx

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
  todayTasksCount: number; // New prop for today's tasks count
  showTodayTasksOnly: boolean; // New prop for filter state
  onToggleShowTodayTasksOnly: () => void; // New prop for toggling filter
}

const Sidebar: React.FC<SidebarProps> = ({
  isOpen,
  onClose,
  todayTasksCount,
  showTodayTasksOnly,
  onToggleShowTodayTasksOnly,
}) => {
  const [showNewListInput, setShowNewListInput] = useState(false);
  const [newListName, setNewListName] = useState('');
  const [showNewTagInput, setShowNewTagInput] = useState(false);
  const [newTagName, setNewTagName] = useState('');

  const handleAddList = () => {
    if (newListName.trim()) {
      console.log('Add new list:', newListName);
      setNewListName('');
      setShowNewListInput(false);
    }
  };

  const handleAddTag = () => {
    if (newTagName.trim()) {
      console.log('Add new tag:', newTagName);
      setNewTagName('');
      setShowNewTagInput(false);
    }
  };

  return (
    <div
      className={`fixed inset-y-0 left-0 w-64 bg-white shadow-lg transform ${
        isOpen ? 'translate-x-0' : '-translate-x-full'
      } lg:translate-x-0 lg:static lg:inset-0 lg:w-64 z-40 transition-transform duration-300 ease-in-out`}
    >
      <div className="flex items-center justify-between p-4 border-b border-gray-200 lg:hidden">
        <h2 className="text-xl font-semibold text-gray-800">Menu</h2>
        <button onClick={onClose} className="text-gray-600 hover:text-gray-900">
          <FontAwesomeIcon icon={faTimes} size="lg" />
        </button>
      </div>
      <div className="p-4 flex flex-col h-[calc(100vh-64px)] overflow-y-auto">
        {/* Search Bar */}
        <div className="mb-6">
          <div className="relative">
            <input
              type="text"
              placeholder="Search..."
              className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
            <FontAwesomeIcon
              icon={faSearch}
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
            />
          </div>
        </div>

        {/* Tasks Section */}
        <div className="mb-6">
          <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Tasks</h3>
          <ul>
            <li className="mb-2">
              <a href="#" className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
                Upcoming Task
              </a>
            </li>
            <li className="mb-2">
              <button
                onClick={onToggleShowTodayTasksOnly}
                className={clsx(
                  "flex items-center justify-between w-full p-2 rounded-md transition-colors duration-200",
                  showTodayTasksOnly
                    ? "bg-indigo-100 text-indigo-800"
                    : "text-gray-700 hover:text-indigo-600 hover:bg-gray-50"
                )}
              >
                <span>Today</span>
                {todayTasksCount > 0 && (
                  <span className="ml-2 px-2 py-0.5 text-xs font-semibold bg-red-500 text-white rounded-full">
                    {todayTasksCount}
                  </span>
                )}
              </button>
            </li>
            <li className="mb-2">
              <a href="#" className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
                Calendar
              </a>
            </li>
            <li className="mb-2">
              <a href="#" className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
                Sticky Wall
              </a>
            </li>
          </ul>
        </div>

        {/* Lists Section */}
        <div className="mb-6">
          <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Lists</h3>
          <ul>
            <li className="mb-2">
              <a href="#" className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
                Personal
              </a>
            </li>
            <li className="mb-2">
              <a href="#" className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
                Work
              </a>
            </li>
            <li className="mb-2">
              <button
                onClick={() => setShowNewListInput(!showNewListInput)}
                className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200 w-full text-left"
              >
                <FontAwesomeIcon icon={faPlus} className="mr-2" /> Add other list
              </button>
              {showNewListInput && (
                <div className="mt-2 flex">
                  <input
                    type="text"
                    value={newListName}
                    onChange={(e) => setNewListName(e.target.value)}
                    onKeyPress={(e) => {
                      if (e.key === 'Enter') handleAddList();
                    }}
                    className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm"
                    placeholder="New list name"
                  />
                  <button onClick={handleAddList} className="ml-2 px-3 py-1.5 bg-indigo-600 text-white rounded-md text-sm hover:bg-indigo-700">
                    Add
                  </button>
                </div>
              )}
            </li>
          </ul>
        </div>

        {/* Tags Section */}
        <div className="mb-6">
          <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Tags</h3>
          <ul>
            <li className="mb-2">
              <a href="#" className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
                Tag 1
              </a>
            </li>
            <li className="mb-2">
              <a href="#" className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
                Tag 2
              </a>
            </li>
            <li className="mb-2">
              <button
                onClick={() => setShowNewTagInput(!showNewTagInput)}
                className="flex items-center text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200 w-full text-left"
              >
                <FontAwesomeIcon icon={faPlus} className="mr-2" /> Add another tag
              </button>
              {showNewTagInput && (
                <div className="mt-2 flex">
                  <input
                    type="text"
                    value={newTagName}
                    onChange={(e) => setNewTagName(e.target.value)}
                    onKeyPress={(e) => {
                      if (e.key === 'Enter') handleAddTag();
                    }}
                    className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm"
                    placeholder="New tag name"
                  />
                  <button onClick={handleAddTag} className="ml-2 px-3 py-1.5 bg-indigo-600 text-white rounded-md text-sm hover:bg-indigo-700">
                    Add
                  </button>
                </div>
              )}
            </li>
          </ul>
        </div>

        {/* Settings Button */}
        <div className="mt-auto pt-4 border-t border-gray-200">
          <button className="flex items-center w-full text-gray-700 hover:text-indigo-600 hover:bg-gray-50 p-2 rounded-md transition-colors duration-200">
            <FontAwesomeIcon icon={faCog} className="mr-3" /> Settings
          </button>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
