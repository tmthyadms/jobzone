<template>
  <label class="block">
    <span
      v-if="label"
      class="text-xs font-semibold capitalize align-top opacity-60"
      >{{ label }} <span v-if="req">*</span></span
    >
    <slot>
      <input
        :type="type"
        :id="newInputId"
        :name="newInputId"
        :placeholder="inputPlaceholder"
        class="form-input app-field"
        :required="req"
        :disabled="disabled"
        :autocomplete="ac"
        :min="type === 'number' ? 0 : null"
        @input="$emit('input', $event.target.value)"
      />
    </slot>
  </label>
</template>

<script>
export default {
  emits: ['input'],
  props: {
    label: {
      type: String,
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
    new: {
      type: Boolean,
    },
    req: {
      type: Boolean,
    },
    disabled: {
      type: Boolean,
    },
    ac: {
      type: String,
      default: 'off',
    },
  },
  computed: {
    newInputId() {
      return this.new ? `new-${this.inputId}` : this.inputId;
    },
    inputPlaceholder() {
      return this.prompt ? this.prompt : 'Enter your ' + this.label;
    },
  },
};
</script>
