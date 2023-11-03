<template>
  <AppCard class="!max-w-none !max-h-none">
    <template #body>
      <AppComboMark class="justify-center lg:justify-start mb-6" />
      <h2
        class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
      >
        Sign in to unlock <br class="hidden lg:inline" />
        your <br class="inline lg:hidden" />secure future
      </h2>
      <form action="" class="grid grid-cols-1 gap-6">
        <AppInput
          label="email"
          type="email"
          input-id="email"
          :req="true"
          ac="email"
        />
        <InputPassword />
        <!-- <button type="submit" name="sign-in" class="btn btn-block btn-primary">
          sign in
        </button> -->
        <NuxtLink to="/home" class="btn btn-block btn-primary">
          sign in
        </NuxtLink>
      </form>
      <NuxtLink
        to="/sign-up"
        class="btn btn-outline btn-primary"
        @click="$emit('flip')"
      >
        new to jobzone? join now</NuxtLink
      >
    </template>
  </AppCard>
</template>

<script>
export default {
  events: ['flip'],
};
</script>
