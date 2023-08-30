$(".delete-cupcake").click(deleteCupcake);

async function deleteCupcake() {
  const id = $(this).data("id");
  await axios.delete(`/api/cupcakes/${id}`);
  $(this).parent().remove();
}

$("#new-cupcake-form").submit(addCupcake);

async function addCupcake(event) {
  event.preventDefault();

  const form = $(this);
  const formInfo = form.serializeArray();
  const newInfo = {};

  formInfo.forEach((field) => {
    newInfo[field.name] = field.value;
  });

  try {
    const response = await axios.post("/api/cupcakes", newInfo);
    const cupcake = response.data.cupcake;

    const cupcakeItem = `<li>${cupcake.flavor} - <button class="delete-cupcake" data-id="${cupcake.id}">X</button></li>`;

    $("ul").append(cupcakeItem);
    form.trigger("reset");
  } catch (err) {
    console.error(err);
  }
}
