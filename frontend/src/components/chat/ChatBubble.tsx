// frontend/src/components/chat/ChatBubble.tsx
'use client';

import { ChatBubbleOvalLeftEllipsisIcon } from '@heroicons/react/24/solid';

interface ChatBubbleProps {
  onClick: () => void;
}

const ChatBubble: React.FC<ChatBubbleProps> = ({ onClick }) => {
  return (
    <button
      onClick={onClick}
      className="fixed bottom-8 right-8 bg-indigo-600 text-white p-4 rounded-full shadow-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 z-50"
      aria-label="Open chat"
    >
      <ChatBubbleOvalLeftEllipsisIcon className="h-8 w-8" />
    </button>
  );
};

export default ChatBubble;
