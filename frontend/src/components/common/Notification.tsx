'use client';

import React from 'react';
import { useApp } from '../../contexts/AppContext';

export const Notification: React.FC = () => {
  const { notification } = useApp();

  if (!notification || !notification.visible) {
    return null;
  }

  const notificationClass =
    notification.type === 'success'
      ? 'bg-green-500 border-green-700'
      : 'bg-red-500 border-red-700';

  return (
    <div
      className={`fixed top-4 right-4 p-4 rounded-md shadow-lg text-white border-l-4 z-[9999] transition-transform duration-300 transform ${
        notification.visible ? 'translate-x-0' : 'translate-x-full'
      } max-w-xs w-full ${notificationClass} !opacity-100`}
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div className="flex items-center">
        <div className="flex-shrink-0">
          {notification.type === 'success' ? (
            <svg
              className="h-6 w-6 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
          ) : (
            <svg
              className="h-6 w-6 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
          )}
        </div>
        <div className="ml-3">
          <p className="text-sm font-medium">{notification.message}</p>
        </div>
      </div>
    </div>
  );
};
