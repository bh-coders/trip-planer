module.exports = function (api) {
  api.cache.using(() => process.env.NODE_ENV);
  return {
    presets: ['module:metro-react-native-babel-preset'],
    plugins: [
      ['module:react-native-dotenv', {
        envName: 'APP_ENV',
        moduleName: '@env',
        path: '../.envs/frontend/.env.development',
        safe: false,
        allowUndefined: true,
        verbose: false,
      }],
      ['react-native-reanimated/plugin'],
      [
        'inline-import-data-uri',
        {
          extensions: ['png'],
        },
      ],
    ],
  };
};
