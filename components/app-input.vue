<template>
  <label class="block">
    <span class="text-xs font-semibold opacity-60 capitalize">{{ label }}</span>
    <slot>
      <input
        :type="type"
        :id="inputId"
        :name="inputId"
        :placeholder="placeholder"
        class="app-input"
      />
    </slot>
  </label>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      default: 'text',
    },
    prompt: {
      type: String,
    },
    inputId: {
      type: String,
    },
  },
  computed: {
    placeholder() {
      return this.prompt ? this.prompt : 'Enter your ' + this.label;
    },
  },
};
</script>

<style scoped></style>
