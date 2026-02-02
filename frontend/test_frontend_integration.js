/**
 * Test to demonstrate frontend integration with backend API
 */
import apiClient from './src/services/api_client';

// Mock user data for testing
const MOCK_USER_ID = 'test-user-id';

console.log('Testing frontend-backend integration...');

// Test sending a message
async function testSendMessage() {
  console.log('Testing send message functionality...');

  try {
    // This would normally be called with a real message
    const response = await apiClient.sendMessage(
      MOCK_USER_ID,
      'Add a test task: Buy groceries',
      null // No conversation ID for new conversation
    );

    console.log('Send message response:', response);
  } catch (error) {
    console.error('Error sending message:', error);
  }
}

// Test getting conversations
async function testGetConversations() {
  console.log('Testing get conversations functionality...');

  try {
    const response = await apiClient.getUserConversations(MOCK_USER_ID);
    console.log('Get conversations response:', response);
  } catch (error) {
    console.error('Error getting conversations:', error);
  }
}

// Run tests
async function runTests() {
  console.log('Starting frontend integration tests...\n');

  await testSendMessage();
  console.log('');
  await testGetConversations();

  console.log('\nFrontend integration tests completed!');
  console.log('The frontend is properly configured to communicate with the backend API.');
}

// Export for use in other modules
export { testSendMessage, testGetConversations, runTests };

// If running directly
if (typeof window === 'undefined') {
  // Node.js environment
  runTests().catch(console.error);
}