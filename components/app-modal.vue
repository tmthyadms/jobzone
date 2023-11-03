<template>
  <dialog :id="modalId" class="modal modal-bottom sm:modal-middle">
    <div class="modal-box">
      <button
        class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2"
        @click="closeModal"
      >
        <IconX />
      </button>
      <h3 class="mb-6 text-2xl lg:text-4xl font-thin">{{ title }}</h3>
      <slot>
        <p>{{ desc }}</p>
      </slot>
    </div>
  </dialog>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    desc: {
      type: String,
    },
    modalId: {
      type: String,
      required: true,
    },
  },
  methods: {
    closeModal() {
      const modal = document.getElementById(this.modalId);
      modal.classList.remove('modal-open');
    },
  },
};
</script>
