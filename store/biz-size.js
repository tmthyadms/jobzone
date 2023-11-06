export const state = () => ({
  bizSize: [
    { name: 'Select your business size', value: '' },
    { name: '1-10', value: '1-10' },
    { name: '11-50', value: '11-50' },
    { name: '51-200', value: '51-200' },
    { name: '201-500', value: '201-500' },
    { name: '501-1000', value: '501-1000' },
    { name: '1001-5000', value: '1001-5000' },
    { name: '5001-10000', value: '5001-10000' },
    { name: '10001+', value: '10001+' },
  ],
});

export const getters = {
  bizSize: (state) => state.bizSize,
};
