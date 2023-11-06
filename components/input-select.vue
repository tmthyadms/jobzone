<template>
  <AppInput :label="label" :req="req">
    <select
      :id="newSelectId"
      :name="newSelectId"
      class="form-select app-field"
      :required="req"
      :autocomplete="ac"
      @change="$emit('change', $event.target.value)"
    >
      <template v-for="(option, index) in options">
        <option
          :key="index"
          :value="option?.value"
          :disabled="index === 0"
          :selected="index === 0"
        >
          {{ option.name }}
        </option>
      </template>
    </select>
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
    selectId: {
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
    options: {
      type: Array,
      required: true,
    },
  },
  computed: {
    newSelectId() {
      return this.new ? `new-${this.selectId}` : this.selectId;
    },
  },
};
</script>
