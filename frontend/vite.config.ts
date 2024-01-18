import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import dotenv from 'dotenv';

const alias = [
  { find: '@', replacement: '/src' },
  { find: 'assets', replacement: '/src/assets' },
  { find: 'components', replacement: '/src/components' },
];

const configBase = {
  plugins: [react()],
  resolve: {
    alias: [...alias],
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
  dotenv.config({ path: '../.envs/.env.development' });
  configType = {
    ...configBase,
    server: {
      ...configBase.server,
      host: '0.0.0.0',
      port: 3000,
    },
  };
} else {
  dotenv.config({ path: '../.envs/.env.production' });
  configType = {
    ...configBase,
    server: {
      ...configBase.server,
      host: process.env.HOST,
      port: Number(process.env.PORT),
    },
  };
}

console.log(process.env.NODE_ENV);
export default defineConfig(configType);
