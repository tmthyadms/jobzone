<template>
  <AppCard class="card-compact">
    <template #body>
      <div>
        <p class="font-semibold">{{ title }}</p>
        <p class="text-sm">{{ subtitle }}</p>
      </div>
      <button
        type="button"
        class="btn btn-xs btn-error btn-square btn-outline"
        @click="$emit('clear')"
      >
        <IconTrash />
      </button>
    </template>
  </AppCard>
</template>

<script>
export default {
  emits: ['clear'],
  props: {
    title: {
      type: String,
      required: true,
    },
    subtitle: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
:deep(.card-body) {
  @apply flex-row items-center justify-between;
}
</style>
