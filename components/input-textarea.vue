<template>
  <AppInput :label="label" :req="req">
    <textarea
      :id="newTextAreaId"
      :name="newTextAreaId"
      :placeholder="inputPlaceholder"
      class="form-textarea app-field"
      :required="req"
      :autocomplete="ac"
      @input="$emit('input', $event.target.value)"
    ></textarea>
  </AppInput>
</template>

<script>
export default {
  emits: ['change'],
  props: {
    label: {
      type: String,
      required: true,
    },
    prompt: {
      type: String,
    },
    textAreaId: {
      type: String,
    },
    new: {
      type: Boolean,
    },
    req: {
      type: Boolean,
    },
    ac: {
      type: String,
      default: 'off',
    },
  },
  computed: {
    newTextAreaId() {
      return this.new ? `new-${this.textAreaId}` : this.selectId;
    },
    inputPlaceholder() {
      return this.prompt ? this.prompt : 'Enter your ' + this.label;
    },
  },
};
</script>
