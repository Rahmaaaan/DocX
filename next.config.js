/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    serverActions: true,
  },
  images: {
    domains: ['tbmrilekqscewxbkjzvh.supabase.co'],
  },
};

module.exports = nextConfig;
