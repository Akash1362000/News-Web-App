const pushForm = document.getElementById('send-push__form');
const errorMsg = document.querySelector('.error');

pushForm.addEventListener('submit', async function (e) {
  e.preventDefault();
  const input = this[0];
  const textarea = this[1];
  const button = this[2];
  errorMsg.innerText = '';

  const head = input.value;
  const body = textarea.value;
  const meta = document.querySelector('meta[name="user_id"]');
  const id = meta ? meta.content : null;

  if (head && body && id) {
    button.innerText = 'Sending...';
    button.disabled = true;

    const res = await fetch('/send_push', {
      method: 'POST',
      body: JSON.stringify({ head, body, id }),
      headers: {
        'content-type': 'application/json',
      },
    });
    if (res.status === 200) {
      button.innerText = 'Send another 😃!';
      button.disabled = false;
      input.value = '';
      textarea.value = '';
    } else {
      errorMsg.innerText = res.message;
      button.innerText = 'Something broke 😢..  Try again?';
      button.disabled = false;
    }
  } else {
    let error;
    if (!head || !body) {
      error = 'Please ensure you complete the form 🙏🏾';
    } else if (!id) {
      error = "Are you sure you're logged in? 🤔. Make sure! 👍🏼";
    }
    errorMsg.innerText = error;
  }
});
