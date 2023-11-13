<template>
  <AppCard class="card-compact">
    <template #body>
      <div :class="{ 'text-[graytext]': disabled }">
        <p class="font-semibold">{{ title }}</p>
        <p class="text-sm">{{ subtitle }}</p>
      </div>
      <div
        :class="{ 'tooltip tooltip-left': !disabled }"
        data-tip="Remove this"
      >
        <button
          type="button"
          class="btn btn-xs btn-error btn-square btn-outline"
          :disabled="disabled"
          @click="$emit('clear')"
        >
          <IconTrash />
        </button>
      </div>
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
    disabled: {
      type: Boolean,
    },
  },
};
</script>

<style scoped>
:deep(.card-body) {
  @apply flex-row items-center justify-between;
}
</style>
