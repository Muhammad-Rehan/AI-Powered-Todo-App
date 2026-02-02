'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useApp } from '../../contexts/AppContext';
import ChatInterface from '../../components/ChatInterface';

const ChatPage = () => {
  const router = useRouter();
  const { user, loadingState } = useApp();
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    if (!loadingState.auth && !user) {
      router.push('/auth/signin');
    } else if (user) {
      setUserId(user.user_id);
    }
  }, [user, loadingState.auth, router]);

  if (loadingState.auth || !userId) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <ChatInterface userId={userId} className="h-screen" />
    </div>
  );
};

export default ChatPage;