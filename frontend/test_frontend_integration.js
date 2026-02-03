/**
 * Test to demonstrate frontend integration with backend API
 */
import apiClient from './src/services/api_client';

// Mock user data for testing
const MOCK_USER_ID = 'test-user-id';


// Test sending a message
async function testSendMessage() {
  try {
    // This would normally be called with a real message
    const response = await apiClient.sendMessage(
      MOCK_USER_ID,
      'Add a test task: Buy groceries',
      null // No conversation ID for new conversation
    );
  } catch (error) {
  }
}

// Test getting conversations
async function testGetConversations() {
  try {
    const response = await apiClient.getUserConversations(MOCK_USER_ID);
  } catch (error) {
  }
}

// Run tests
async function runTests() {
  await testSendMessage();
  await testGetConversations();
}

// Export for use in other modules
export { testSendMessage, testGetConversations, runTests };

// If running directly
if (typeof window === 'undefined') {
  // Node.js environment
  runTests();
}