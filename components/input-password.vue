<template>
  <AppInput label="password">
    <div class="relative">
      <input
        :type="passwordType"
        :id="passwordId"
        placeholder="Enter your password"
        class="app-input pr-5"
      />

      <div
        class="tooltip tooltip-left absolute end-0 top-1/2"
        style="translate: 0 -50%"
        :data-tip="passwordTip"
      >
        <label role="button" class="btn btn-xs btn-ghost btn-circle swap">
          <input type="checkbox" v-model="password.reveal" />
          <IconEye class="swap-on" />
          <IconEyeSlash class="swap-off" />
        </label>
      </div>
    </div>
  </AppInput>
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
  props: {
    new: {
      type: Boolean,
    },
  },
  computed: {
    passwordType() {
      return this.password.reveal
        ? this.password.show.type
        : this.password.hide.type;
    },
    passwordId() {
      return this.new ? `${this.new}-password` : 'password';
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

<style scoped></style>
