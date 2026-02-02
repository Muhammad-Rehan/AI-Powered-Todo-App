import './globals.css';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { AppProvider } from '../contexts/AppContext';
import { Notification } from '../components/common/Notification'; // Import Notification component


const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Todo Web Application',
  description: 'An AI-powered chatbot todo application that helps users manage tasks with natural language.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AppProvider>
          {children}
          <Notification /> {/* Render Notification component */}
        </AppProvider>
      </body>
    </html>
  );
}