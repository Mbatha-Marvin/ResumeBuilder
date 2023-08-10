<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">Education</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <p class="d-inline">Create New Education
                                    <NuxtLink :to="'/resume/education'" class="btn btn-sm btn-danger float-end"><i class="bi bi-arrow-left-circle"></i>Back
                                    </NuxtLink>
                                </p>
                            </div>
                            <div class="card">
                                <div class="card-body">
                                    <form class="form form-horizontal">
                                        <div class="form-body">
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="course_title">Course
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="course_title"
                                                                class="form-control border-primary" placeholder="Course Title" name="course_title">
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="col-md-6 invisible">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="card_title">Card
                                                            Title</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="card_title"
                                                                class="form-control border-primary" value="Education" placeholder="Card Title"
                                                                name="card_title">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="school_name">School
                                                            Name</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="school_name"
                                                                class="form-control border-primary" placeholder="School Name" name="school_name">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="location">Location</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="location"
                                                                class="form-control border-primary" placeholder="Location"
                                                                name="location">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control"
                                                            for="education_level">Education Level</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="education_level"
                                                                class="form-control border-primary" placeholder="Education Level" name="education_level">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="final_grade">Final
                                                            Grade</label>
                                                        <div class="col-md-9">
                                                            <input type="text" id="final_grade"
                                                                class="form-control border-primary" placeholder="Final Grade" name="final_grade">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="start_date">Start
                                                            Date</label>
                                                        <div class="col-md-9">
                                                            <input type="date" id="start_date"
                                                                class="form-control border-primary" placeholder="Start
                                                            Date" name="start_date">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <div class="form-group row mb-2">
                                                        <label class="col-md-3 label-control" for="end_date">End
                                                            date</label>
                                                        <div class="col-md-9">
                                                            <input type="date" id="end_date"
                                                                class="form-control border-primary" placeholder="End date"
                                                                name="end_date">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="form-actions float-end mt-2">
                                            <NuxtLink :to="'/resume/education/create'" class="btn btn-danger mx-2">
                                                <i class="bi bi-x-lg"></i> Cancel
                                            </NuxtLink>
                                            <button type="submit" class="btn btn-primary mx-2">
                                                <i class="bi bi-check2-square"></i> Save
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
definePageMeta({
    layout: "sidestar",
})
</script>
  
<style>
.col-md-2,
.col-md-8 {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* For desktop view */
.prev-link,
.next-link {
    display: inline-block;
    padding: 8px 16px;
    background-color: green;
    border: 2px solid green;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    transition: background-color 0.3s, border-color 0.3s;
}

.prev-link:hover,
.next-link:hover {
    background-color: purple;
    border-color: gold;
    border-radius: 10px;
}

/* For mobile view */
@media (max-width: 767.98px) {

    .col-md-2,
    .col-md-8 {
        display: block;
    }

    .prev-link,
    .next-link {
        display: block;
        margin: 10px auto;
        text-align: center;
    }

    .prev-link {
        order: -1;
    }
}
</style>
  