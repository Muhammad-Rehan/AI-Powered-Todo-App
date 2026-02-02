import React from 'react';
import Link from 'next/link';
import { useApp } from '../contexts/AppContext';

const Navbar = () => {
  const { user, signOut } = useApp();

  return (
    <nav className="bg-indigo-600 text-white shadow-md">
      <div className="container mx-auto px-4 py-3">
        <div className="flex justify-between items-center">
          <Link href="/" className="text-xl font-bold">
            Todo App
          </Link>

          <div className="flex items-center space-x-4">
            {user ? (
              <>
                <Link
                  href="/chat"
                  className="bg-green-500 hover:bg-green-600 px-4 py-2 rounded-md text-sm font-medium transition-colors mr-2"
                >
                  AI Chat
                </Link>
                <span className="text-sm">Welcome, {user.email}</span>
                <button
                  onClick={signOut}
                  className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded-md text-sm transition-colors"
                >
                  Sign Out
                </button>
              </>
            ) : (
              <div className="flex space-x-2">
                <Link
                  href="/auth/signin"
                  className="bg-white text-indigo-600 px-4 py-2 rounded-md text-sm font-medium hover:bg-gray-100 transition-colors"
                >
                  Sign In
                </Link>
                <Link
                  href="/auth/signup"
                  className="bg-indigo-700 hover:bg-indigo-800 px-4 py-2 rounded-md text-sm font-medium transition-colors"
                >
                  Sign Up
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;