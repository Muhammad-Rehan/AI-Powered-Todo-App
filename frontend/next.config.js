/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // This enables static exports for GitHub Pages

  // Optional: Add a base path if your site will be hosted at a subdirectory
  // basePath: '/Full-Stack-Todo-Web-Application', // Commented out for local development

  trailingSlash: true, // Recommended for GitHub Pages

  // Images: Since we're exporting statically, we need to handle images properly
  images: {
    unoptimized: true, // This ensures images work in static exports
  },

  // Experimental features (if needed)
  reactStrictMode: true,
}

module.exports = nextConfig