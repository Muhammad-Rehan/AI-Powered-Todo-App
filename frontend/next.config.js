/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // This enables static exports for GitHub Pages

  // Add a base path for GitHub Pages deployment
  basePath: '/AI-Powered-Todo-App',

  trailingSlash: true, // Recommended for GitHub Pages

  // Images: Since we're exporting statically, we need to handle images properly
  images: {
    unoptimized: true, // This ensures images work in static exports
  },

  // Experimental features (if needed)
  reactStrictMode: true,
}

module.exports = nextConfig