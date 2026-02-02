// frontend/src/services/api.ts

export interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
  user_id: string;
}

class ApiService {
  private baseUrl =
    process.env.NEXT_PUBLIC_API_BASE_URL ??
    "http://127.0.0.1:8000";  // Default to local during development

  private async request(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<any> {
    const url = `${this.baseUrl}${endpoint}`;
    console.log(url);
    const headers: HeadersInit = {
      ...(options.headers || {}),
    };

    if (options.body) {
      headers["Content-Type"] = "application/json";
    }

    let response: Response;

    try {
      response = await fetch(url, {
        ...options,
        headers,
      });
    } catch (error) {
      // Network / CORS / DNS errors must propagate
      throw error;
    }

    // ---- Non-OK responses ----
    if (!response.ok) {
      let message = `HTTP ${response.status}`;

      try {
        const data = await response.json();
        message = data.detail ?? message;
      } catch {
        // ignore
      }

      throw new Error(message);
    }

    // ---- No content ----
    if (response.status === 204) {
      return null;
    }

    // ---- Always return parsed JSON ----
    return await response.json();
  }

  // ------------------------------
  // Authentication
  // ------------------------------
  async signIn(email: string, password: string) {
    return await this.request("/api/auth/signin", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
  }

  async signUp(email: string, password: string) {
    return await this.request("/api/auth/signup", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
  }

  signOut() {
    return Promise.resolve();
  }

  // ------------------------------
  // Tasks
  // ------------------------------
  async getTasks(token: string) {
    return await this.request("/api/tasks/", {
      headers: { Authorization: `Bearer ${token}` },
    });
  }

  async getTaskById(taskId: string, token: string) {
    return await this.request(`/api/tasks/${taskId}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
  }

  async createTask(
    taskData: Omit<Task, "id" | "created_at" | "updated_at" | "user_id">,
    token: string
  ) {
    return await this.request("/api/tasks/", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
      body: JSON.stringify(taskData),
    });
  }

  async updateTask(taskId: string, taskData: Partial<Task>, token: string) {
    return await this.request(`/api/tasks/${taskId}`, {
      method: "PUT",
      headers: { Authorization: `Bearer ${token}` },
      body: JSON.stringify(taskData),
    });
  }

  async deleteTask(taskId: string, token: string) {
    return await this.request(`/api/tasks/${taskId}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` },
    });
  }

  async toggleTaskCompletion(taskId: string, token: string) {
    return await this.request(`/api/tasks/${taskId}/toggle`, {
      method: "PATCH",
      headers: { Authorization: `Bearer ${token}` },
    });
  }
}

export const apiService = new ApiService();
