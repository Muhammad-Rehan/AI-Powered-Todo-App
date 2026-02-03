# Backend Configuration for GitHub Pages Deployment

To connect your frontend deployed on GitHub Pages to your Vercel backend, you need to configure the following environment variables in your GitHub repository settings:

## Repository Secrets to Add

Go to your GitHub repository → Settings → Secrets and variables → Actions, and add these secrets:

- `NEXT_PUBLIC_BACKEND_URL`: `https://ai-powered-todo-app-backend.vercel.app/`
- `NEXT_PUBLIC_API_BASE_URL`: `https://ai-powered-todo-app-backend.vercel.app`
- `NEXT_PUBLIC_BETTER_AUTH_URL`: `https://ai-powered-todo-app-backend.vercel.app/`

## Alternative Approach

Alternatively, you can modify the GitHub Actions workflow to inject these values during the build process. The workflow should:

1. Create a `.env.local` file (which is gitignored) during the build process with the correct URLs
2. This file will be used during the Next.js build

The frontend application is already configured to use these environment variables throughout the codebase for API calls and authentication.