export default function ({ store, redirect }) {
  const hasSignedIn = store.getters['auth/hasSignedIn'];
  if (!hasSignedIn) return redirect('/');
}
