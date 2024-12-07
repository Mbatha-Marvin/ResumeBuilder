<template>
  <PartialsHeader title="Language Section">
    <div class="row">
      <p class="d-inline">
        Create New Language
        <NuxtLink :to="'/resume/language'" class="btn btn-sm btn-success float-end"><i class="bi bi-list-ol"></i>{{ " "
          }}List
        </NuxtLink>
      </p>
    </div>
    <div class="card">
      <div class="card-body">
        <form @submit.prevent="CreatenewLanguage" class="form form-horizontal needs-validation" novalidate>
          <div class="form-body">
            <div class="row">
              <div class="col-md-4">
                <div class="form-group mb-2">
                  <label class="label-control" for="card_title">Card Title</label>
                  <select v-model="newLanguage.card_title" class="form-select border-primary"
                    aria-label="Default select example" required>
                    <option disabled value="">Please Select</option>
                    <option>Language</option>
                    <option>Spoken Language</option>
                  </select>
                  <span class="invalid-feedback">Please Select Card Title</span>
                </div>
              </div>

              <div class="col-md-4">
                <div class="form-group mb-2">
                  <label class="label-control" for="language_name">Language Name</label>
                  <input v-model="newLanguage.language_name" type="text" id="language_name"
                    class="form-control border-primary" placeholder="Language Name" name="language_name" required />
                  <span class="invalid-feedback">Language Name is required</span>
                </div>
              </div>

              <div class="col-md-4">
                <div class="form-group mb-2">
                  <label class="label-control" for="profeciency_level">Proficiency Level</label>
                  <select v-model="newLanguage.profeciency_level" class="form-select border-primary"
                    aria-label="Proficiency Level" required>
                    <option disabled value="">Please Select</option>
                    <option v-for="level in levels" :key="level" :value="level">
                      {{ level }}
                    </option>
                  </select>
                  <span class="invalid-feedback">Please select proficiency level</span>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="form-actions my-2">
                <NuxtLink :to="'/resume/language'" class="btn btn-sm btn-danger mx-2 float-start">
                  <i class="bi bi-x-lg"></i>{{ " " }}Cancel
                </NuxtLink>
                <button type="submit" class="btn btn-sm btn-success mx-2 float-end">
                  <i class="bi bi-check2-square"></i>{{ loadingStates ? " Saving..." : " Save" }}
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>

  </PartialsHeader>

</template>

<script>
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "CreateLanguage",
  setup() {
    const { $showToast, $axios } = useNuxtApp();
    const newLanguage = ref({});
    const router = useRouter();
    const loadingStates = ref(false);
    const levels = Array.from({ length: 10 }, (_, i) => i + 1);

    definePageMeta({
      layout: "sidestar",
    });

    useHead({
      title: "Create Language",
      meta: [
        { name: "description", content: "Form to Create Language" },
        { property: "og:title", content: "Create Language" },
        { property: "og:description", content: "Form to Create Language." },
      ],
    });

    const CreatenewLanguage = async () => {
      loadingStates.value = true;
      const form = document.querySelector(".needs-validation");
      const user_id = 1;
      if (form.checkValidity()) {
        try {
          loadingStates.value = true;
          const response = await $axios.post(`/user/${user_id}/language/`, newLanguage.value);
          loadingStates.value = false;
          $showToast("Language created!");
          router.push("/resume/language");
          console.log(response);
        } catch (error) {
          loadingStates.value = false;
          console.log(error);
        }

      } else {
        form.classList.add("was-validated");
      }
    };

    onMounted(() => {
      const forms = document.querySelectorAll(".needs-validation");

      Array.from(forms).forEach((form) => {
        form.addEventListener(
          "submit",
          (event) => {
            event.preventDefault();
            event.stopPropagation();

            if (!form.checkValidity()) {
              form.classList.add("was-validated");
            } else {
              CreatenewLanguage();
            }
          },
          false
        );
      });
    });

    return {
      newLanguage,
      loadingStates,
      levels,
    };
  },
});
</script>

<style></style>
