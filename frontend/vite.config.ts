import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import dotenv from 'dotenv';

const alias = [
  { find: '@', replacement: '/src' },
  { find: 'assets', replacement: '/src/assets' },
  { find: 'components', replacement: '/src/components' },
];

const extensions = [
  '.web.tsx',
  '.tsx',
  '.web.ts',
  '.ts',
  '.web.jsx',
  '.jsx',
  '.web.js',
  '.js',
  '.css',
  '.json',
  '.mjs',
];

const configBase = {
  clearScreen: true,
  plugins: [react()],
  resolve: {
    extensions: extensions,
    alias: [
      {
        find: 'react-native',
        replacement: 'react-native-web',
      },
      ...alias,
    ],
  },
  server: {
    watch: {
      usePolling: true,
    },
  },
  define: {
    'process.env': process.env,
  },
};

let configType = {};
if (process.env.NODE_ENV === 'development') {
  dotenv.config({ path: '../.envs/frontend/.env.development' });
  configType = {
    ...configBase,
    server: {
      ...configBase.server,
      host: '0.0.0.0',
      port: 3000,
    },
  };
} else {
  dotenv.config({ path: '../.envs/frontend/.env.production' });
  configType = {
    ...configBase,
    server: {
      ...configBase.server,
      host: process.env.HOST,
      port: Number(process.env.PORT),
    },
  };
}

export default defineConfig(configType);
