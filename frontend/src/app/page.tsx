'use client';

import Link from 'next/link';
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useApp } from '../contexts/AppContext';

export default function HomePage() {
  const router = useRouter();
  const { user, loadingState } = useApp();

  useEffect(() => {
    if (!loadingState.auth && user) {
      router.push('/dashboard');
    }
  }, [user, loadingState, router]);

  if (loadingState.auth) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Checking authentication status...</p>
        </div>
      </div>
    );
  }

  if (user) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex flex-col">
      {/* Navigation */}
      <nav className="flex items-center justify-between p-6 max-w-7xl mx-auto w-full">
        <div className="text-2xl font-bold text-indigo-700 tracking-wide">TaskFlow</div>
        <div className="flex space-x-3">
          <Link
            href="/auth/signin"
            className="px-5 py-2 text-indigo-600 hover:text-indigo-800 font-medium rounded-lg hover:bg-indigo-50 transition"
          >
            Login
          </Link>
          <Link
            href="/auth/signup"
            className="px-5 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 font-medium transition"
          >
            Sign Up
          </Link>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="flex-1 flex flex-col justify-center px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center max-w-4xl mx-auto">
          <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-gray-900 mb-6">
            An AI Powered Chatbot that helps you with your daily tasks with{' '}
            <span className="text-indigo-600">TaskFlow</span>
          </h1>

          <p className="text-lg sm:text-xl md:text-2xl text-gray-700 mb-8 max-w-3xl mx-auto">
            An intuitive AI Chatbot that helps you manage tasks, boost productivity, and achieve your goals effortlessly by just chatting with it.
          </p>

          <div className="flex flex-col sm:flex-row justify-center items-center gap-4 sm:gap-6">
            <Link
              href="/auth/signup"
              className="px-8 py-3 bg-indigo-600 text-white font-semibold rounded-lg shadow-lg hover:bg-indigo-700 transition w-full sm:w-auto text-center"
            >
              Get Started - It's Free
            </Link>
            <Link
              href="/auth/signin"
              className="px-8 py-3 bg-white text-indigo-600 font-semibold rounded-lg shadow border border-indigo-200 hover:bg-indigo-50 transition w-full sm:w-auto text-center"
            >
              Sign In
            </Link>
            <Link
              href="/chat"
              className="px-8 py-3 bg-green-600 text-white font-semibold rounded-lg shadow-lg hover:bg-green-700 transition w-full sm:w-auto text-center"
            >
              Try AI Chat
            </Link>
          </div>
        </div>

        {/* Features Section */}
        <section className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8">
          {[
            {
              title: 'Task Organization',
              desc: 'Create, categorize, and prioritize tasks with ease. Keep your daily workflow clear and organized.',
              icon: (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6 text-indigo-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2"
                  />
                </svg>
              ),
            },
            {
              title: 'Time Management',
              desc: 'Set due dates, reminders, and time estimates to stay on top of your schedule.',
              icon: (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6 text-indigo-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              ),
            },
            {
              title: 'Progress Tracking',
              desc: 'Visualize your productivity and celebrate achievements to maintain motivation.',
              icon: (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6 text-indigo-600"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              ),
            },
          ].map((feature) => (
            <div
              key={feature.title}
              className="bg-white p-6 rounded-2xl shadow-lg text-center flex flex-col items-center hover:scale-105 transition-transform"
            >
              <div className="w-16 h-16 bg-indigo-50 rounded-full flex items-center justify-center mb-4">
                {feature.icon}
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600 text-sm">{feature.desc}</p>
            </div>
          ))}
        </section>

        {/* CTA Section */}
        <section className="mt-20 bg-white/80 backdrop-blur-md rounded-3xl p-10 text-center shadow-xl">
          <h2 className="text-2xl sm:text-3xl font-bold text-gray-900 mb-4">
            Ready to Transform Your Productivity?
          </h2>
          <p className="text-gray-700 mb-6 max-w-xl mx-auto text-base sm:text-lg">
            Join thousands of users who have transformed their daily routine with
            TaskFlow. Start organizing your tasks today.
          </p>

          <div className="flex flex-col sm:flex-row justify-center items-center gap-4">
            <Link
              href="/auth/signup"
              className="px-8 py-3 bg-indigo-600 text-white font-semibold rounded-lg shadow-lg hover:bg-indigo-700 transition w-full sm:w-auto text-center"
            >
              Create Free Account
            </Link>
            <Link
              href="/auth/signin"
              className="px-8 py-3 bg-white border-2 border-indigo-600 text-indigo-600 font-semibold rounded-lg hover:bg-indigo-50 transition w-full sm:w-auto text-center"
            >
              Sign In to Account
            </Link>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="py-6 text-center text-gray-500 text-sm border-t border-gray-200 mt-auto">
        © {new Date().getFullYear()} TaskFlow. Made by Muhammad Rehan. All rights reserved.
      </footer>
    </div>
  );
}
