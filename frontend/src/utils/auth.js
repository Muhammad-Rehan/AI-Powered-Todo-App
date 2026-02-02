/**
 * Utility functions for handling JWT authentication in the frontend
 */

// Function to save JWT token to localStorage
export const saveToken = (token) => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('authToken', token);
  }
};

// Function to retrieve JWT token from localStorage
export const getToken = () => {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('authToken');
  }
  return null;
};

// Function to remove JWT token from localStorage
export const removeToken = () => {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('authToken');
  }
};

// Function to check if token exists
export const hasToken = () => {
  const token = getToken();
  return token !== null && token !== undefined && token !== '';
};

// Function to decode JWT token to get user information
export const decodeToken = (token) => {
  if (!token) {
    return null;
  }

  try {
    // Remove 'Bearer ' prefix if present
    const cleanToken = token.startsWith('Bearer ') ? token.substring(7) : token;

    // Split the token into parts
    const parts = cleanToken.split('.');

    if (parts.length !== 3) {
      console.error('Invalid token format');
      return null;
    }

    // Decode the payload (second part)
    const payload = parts[1];
    // Add padding if needed
    const paddedPayload = payload.replace(/-/g, '+').replace(/_/g, '/');
    const decodedPayload = atob(paddedPayload);

    return JSON.parse(decodedPayload);
  } catch (error) {
    console.error('Error decoding token:', error);
    return null;
  }
};

// Function to get user ID from token
export const getUserIdFromToken = () => {
  const token = getToken();
  if (!token) {
    return null;
  }

  const decoded = decodeToken(token);
  return decoded ? decoded.sub : null; // 'sub' is typically the user ID in JWT
};

// Function to check if token is expired
export const isTokenExpired = (token) => {
  const decoded = decodeToken(token);

  if (!decoded || !decoded.exp) {
    return true; // If no expiration, consider it expired
  }

  const currentTime = Math.floor(Date.now() / 1000); // Current time in seconds
  return decoded.exp < currentTime;
};

// Function to check if token is about to expire (within 5 minutes)
export const isTokenExpiringSoon = (token) => {
  const decoded = decodeToken(token);

  if (!decoded || !decoded.exp) {
    return true; // If no expiration, consider it expiring soon
  }

  const currentTime = Math.floor(Date.now() / 1000); // Current time in seconds
  const fiveMinutesInSeconds = 5 * 60;

  return decoded.exp - currentTime < fiveMinutesInSeconds;
};

// Function to add JWT token to request headers
export const addAuthHeader = (headers = {}) => {
  const token = getToken();

  if (token && !isTokenExpired(token)) {
    return {
      ...headers,
      'Authorization': `Bearer ${token}`
    };
  }

  return headers;
};

// Function to refresh token if needed
export const ensureValidToken = async () => {
  const token = getToken();

  if (!token) {
    return false; // No token available
  }

  if (isTokenExpired(token)) {
    // Token is expired, need to refresh or redirect to login
    removeToken();
    // In a real app, you might want to redirect to login page
    // window.location.href = '/login';
    return false;
  } else if (isTokenExpiringSoon(token)) {
    // Token is about to expire, might want to refresh it
    // This would involve calling a refresh endpoint
    // await refreshToken();
  }

  return true; // Token is valid
};

// Function to get token expiration time
export const getTokenExpiration = (token) => {
  const decoded = decodeToken(token);

  if (!decoded || !decoded.exp) {
    return null;
  }

  // Return expiration time as Date object
  return new Date(decoded.exp * 1000);
};

// Function to get time until token expiration
export const getTimeUntilExpiration = (token) => {
  const expiration = getTokenExpiration(token);

  if (!expiration) {
    return null;
  }

  const currentTime = new Date();
  const timeDiff = expiration.getTime() - currentTime.getTime();

  return timeDiff > 0 ? timeDiff : 0; // Return 0 if already expired
};