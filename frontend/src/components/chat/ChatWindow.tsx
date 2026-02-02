// frontend/src/components/chat/ChatWindow.tsx
'use client';

import { XMarkIcon } from '@heroicons/react/24/solid';
import ChatInterface from '../ChatInterface';

interface ChatWindowProps {
  userId: string;
  onClose: () => void;
  onTaskAdded: () => void;
  onTaskRemovedFromState: (id: string) => void; // Changed from onTaskDeleted
}

const ChatWindow: React.FC<ChatWindowProps> = ({ userId, onClose, onTaskAdded, onTaskRemovedFromState }) => {
  return (
    <div className="fixed bottom-4 right-4 w-96 h-5/6 max-h-[30rem] bg-white rounded-xl shadow-2xl flex flex-col z-50">
      <header className="bg-indigo-600 text-white p-2 flex justify-between items-center rounded-t-xl">
        <h2 className="text-lg font-bold">AI Assistant</h2>
        <button
          onClick={onClose}
          className="p-1 rounded-full hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-white"
          aria-label="Close chat"
        >
          <XMarkIcon className="h-6 w-6" />
        </button>
      </header>
      <div className="flex-grow overflow-y-auto">
        <ChatInterface userId={userId} className="h-full" showSidebar={false} onTaskAdded={onTaskAdded} onTaskRemovedFromState={onTaskRemovedFromState} />
      </div>
    </div>
  );
};

export default ChatWindow;
