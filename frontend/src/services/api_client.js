import axios from 'axios';

class ApiClient {
  constructor() {
    this.baseURL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';
    this.client = axios.create({
      baseURL: this.baseURL,
      timeout: 30000, // 30 seconds timeout
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Request interceptor to add auth token
    this.client.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('authToken');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Response interceptor for error handling
    this.client.interceptors.response.use(
      (response) => response,
      (error) => {
        // Handle specific error cases
        if (error.response?.status === 401) {
          // Redirect to login if unauthorized
          localStorage.removeItem('authToken');
          window.location.href = '/login';
        }

        return Promise.reject(error);
      }
    );
  }

  // Chat API methods
  async sendMessage(userId, message, conversationId = null) {
    try {
      const response = await this.client.post(`/api/v1/api/${userId}/chat`, {
        message,
        conversation_id: conversationId
      });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async getUserConversations(userId) {
    try {
      const response = await this.client.get(`/api/v1/api/${userId}/conversations`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async getConversationMessages(userId, conversationId) {
    try {
      const response = await this.client.get(`/api/v1/api/${userId}/conversations/${conversationId}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  // Task API methods (if needed separately from chat)
  async createTask(userId, taskData) {
    try {
      const response = await this.client.post(`/api/${userId}/tasks`, taskData);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async getTasks(userId, filters = {}) {
    try {
      const params = new URLSearchParams(filters);
      const response = await this.client.get(`/api/${userId}/tasks?${params}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async updateTask(userId, taskId, taskData) {
    try {
      const response = await this.client.put(`/api/${userId}/tasks/${taskId}`, taskData);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async deleteTask(userId, taskId) {
    try {
      const response = await this.client.delete(`/api/${userId}/tasks/${taskId}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  // Helper method to handle errors consistently
  handleError(error) {
    if (error.response) {
      // Server responded with error status
      const { status, data } = error.response;
      return {
        success: false,
        status,
        message: data.detail || data.message || 'An error occurred',
        error: error.response.data
      };
    } else if (error.request) {
      // Request was made but no response received
      return {
        success: false,
        status: null,
        message: 'Network error: Unable to reach the server',
        error: 'Network error'
      };
    } else {
      // Something else happened
      return {
        success: false,
        status: null,
        message: error.message || 'An unexpected error occurred',
        error: error.message
      };
    }
  }

  // Method to set auth token
  setAuthToken(token) {
    localStorage.setItem('authToken', token);
  }

  // Method to clear auth token
  clearAuthToken() {
    localStorage.removeItem('authToken');
  }

  // Method to get auth token
  getAuthToken() {
    return localStorage.getItem('authToken');
  }
}

// Export a singleton instance
const apiClient = new ApiClient();
export default apiClient;