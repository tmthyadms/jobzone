<template>
  <AppInput>
    <div class="relative">
      <input
        type="search"
        :id="searchId"
        :name="searchId"
        :placeholder="prompt"
        class="form-input app-field pr-5"
        :disabled="disabled"
        @input="$emit('input', $event.target.value)"
      />
      <IconSearch class="absolute end-0 top-1/2" style="translate: 0 -50%" />
    </div>
  </AppInput>
</template>

<script>
export default {
  emits: ['input'],
  props: {
    prompt: {
      type: String,
      default: 'Enter your search',
    },
    searchId: {
      type: String,
    },
    new: {
      type: Boolean,
    },
    disabled: {
      type: Boolean,
    },
  },
};
</script>
