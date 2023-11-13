<template>
  <div class="flex justify-between">
    <label class="block">
      <span class="text-xs font-semibold capitalize align-top opacity-60"
        >{{ label }} <span v-if="req">*</span></span
      >
    </label>
    <div :class="{ 'tooltip tooltip-left': !disabled }" :data-tip="tip">
      <button
        type="button"
        class="btn btn-xs btn-square"
        :disabled="disabled"
        @click="showModal"
      >
        <IconPlus />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      required: true,
    },
    req: {
      type: Boolean,
    },
    tip: {
      type: String,
      required: true,
    },
    modalId: {
      type: String,
      required: true,
    },
    disabled: {
      type: Boolean,
    },
  },
  methods: {
    showModal() {
      const modal = document.getElementById(this.modalId);
      modal.classList.add('modal-open');
    },
  },
};
</script>
