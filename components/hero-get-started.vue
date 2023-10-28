<template>
  <AppHero
    desc='Welcome to Jobzone, where your job search is safeguarded by cutting-edge machine learning, <br class="inline lg:hidden"/>ensuring a fraud-free experience.'
    :loose="true"
    img="images/pass-job-form-6000x4000.jpg"
    :center="false"
  >
    <template #side>
      <div
        class="animated fadeInUp flex-1 border border-base-content border-opacity-5 shadow-inner w-full lg:w-96"
      >
        <AppCard class="!max-w-none !max-h-none">
          <template #body>
            <div
              class="flex items-center justify-center lg:justify-start gap-2 mb-6"
            >
              <img src="images/logo/jz-32.png" alt="" class="app-img" />
              <span href="#" class="font-bold text-xl normal-case"
                >Job<span class="text-primary">zone</span></span
              >
            </div>
            <h2
              class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
            >
              Sign in to <br class="hidden lg:inline" />
              your account
            </h2>
            <form action="" class="grid grid-cols-1 gap-6">
              <label class="block">
                <span class="text-xs font-semibold opacity-60 capitalize"
                  >username</span
                >
                <input
                  type="text"
                  id="username"
                  placeholder="Enter your username"
                  class="app-input"
                />
              </label>
              <label class="block">
                <span class="text-xs font-semibold opacity-60 capitalize"
                  >password</span
                >
                <div class="relative">
                  <input
                    :type="passwordType"
                    id="password"
                    placeholder="Enter your password"
                    class="app-input pr-5"
                  />

                  <div
                    class="tooltip tooltip-left absolute end-0 top-1/2"
                    style="translate: 0 -50%"
                    :data-tip="passwordTip"
                  >
                    <label
                      role="button"
                      class="btn btn-xs btn-ghost btn-circle swap"
                    >
                      <input type="checkbox" v-model="password.reveal" />
                      <IconEye class="swap-on" />
                      <IconEyeSlash class="swap-off" />
                    </label>
                  </div>
                </div>
              </label>
              <button type="submit" class="btn btn-block btn-primary">
                sign in
              </button>
            </form>
            <button type="button" class="btn btn-outline btn-primary">
              new to jobzone? join now
            </button>
          </template>
        </AppCard>
      </div>
    </template>
  </AppHero>
</template>

<script>
export default {
  data() {
    return {
      password: {
        show: {
          type: 'text',
          tip: 'Click to show password',
        },
        hide: {
          type: 'password',
          tip: 'Click to hide password',
        },
        reveal: false,
      },
    };
  },
  computed: {
    passwordType() {
      return this.password.reveal
        ? this.password.show.type
        : this.password.hide.type;
    },
    passwordTip() {
      return this.password.reveal
        ? this.password.hide.tip
        : this.password.show.tip;
    },
    passwordIcon() {
      return this.password.reveal
        ? this.password.show.icon
        : this.password.hide.icon;
    },
  },
};
</script>
