<template>
    <div class="container">
        <div class="modal modal-fullscreen-sm-down fade" id="profileModal" tabindex="-1" aria-labelledby="profileModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="profileModalLabel">Update your personal information</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="recipient-name" class="col-form-label">Recipient:</label>
                                <input type="text" class="form-control" id="recipient-name">
                            </div>
                            <div class="mb-3">
                                <label for="message-text" class="col-form-label">Message:</label>
                                <textarea class="form-control" id="message-text"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        <button type="button" class="btn btn-primary">Save</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div>
                    <div class="card mb-2">
                        <div class="card-body rounded">
                            <h4 class="text-center text-uppercase bold">Personal Information</h4>
                        </div>
                    </div>
                    <div class="card mb-2">
                        <div class="card-content collapse show">
                            <div class="card-body card-dashboard">
                                <div class="row">
                                    <p class="d-inline">Update to match your current information. Ensure you fill all
                                        required fields marked with (*)
                                        <NuxtLink class="btn btn-sm btn-success float-end" data-bs-toggle="modal"
                                            data-bs-target="#profileModal"><i class="bi bi-pencil-square"></i>Update
                                        </NuxtLink>
                                    </p>
                                </div>
                                <div class="row">
                                    <div class="col-md-4">
                                        <div class="row mb-2">
                                            <label class="col-md-3 label-control" for="userinput1">Fist Name</label>
                                            <div class="col-md-9">
                                                <p>akkakak</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="row mb-2">
                                            <label class="col-md-3 label-control" for="userinput2">Last Name</label>
                                            <div class="col-md-9">
                                                <div class="col-md-9">
                                                    <p>akkakak</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <div class="row mb-2">
                                            <label class="col-md-3 label-control" for="userinput2">Last Name</label>
                                            <div class="col-md-9">
                                                <div class="col-md-9">
                                                    <p>akkakak</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                </div>
                                <!-- <div class="table-responsive">
                                    <table class="table table-striped table-bordered zero-configuration">
                                        <thead>
                                            <tr>
                                                <th>FirstName</th>
                                                <th>LastName</th>
                                                <th>MiddleName</th>
                                                <th>City</th>
                                                <th>Country</th>
                                                <th>Address</th>
                                                <th>JobTitle</th>
                                                <th>JobSummary</th>
                                                <th>Objective</th>
                                                <th>Image</th>
                                                <th>LinkInUrl</th>
                                                <th>GithubUrl</th>
                                                <th>WebsiteUrl</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>Tiger</td>
                                                <td>Nixon</td>
                                                <td>Major</td>
                                                <td>Abuja</td>
                                                <td>Niger</td>
                                                <td>2636,Barma</td>
                                                <td>Database Engineer</td>
                                                <td>2 years experience working on dynamic database</td>
                                                <td>seeking job to improve database</td>
                                                <td>Image</td>
                                                <td>LinkedIn link</td>
                                                <td>Github url</td>
                                                <td>personal website url</td>
                                            </tr>
                                        </tbody>
                                        <tfoot>
                                            <tr>
                                                <th>FirstName</th>
                                                <th>LastName</th>
                                                <th>MiddleName</th>
                                                <th>City</th>
                                                <th>Country</th>
                                                <th>Address</th>
                                                <th>JobTitle</th>
                                                <th>JobSummary</th>
                                                <th>Objective</th>
                                                <th>Image</th>
                                                <th>LinkInUrl</th>
                                                <th>GithubUrl</th>
                                                <th>WebsiteUrl</th>
                                            </tr>
                                        </tfoot>
                                    </table>
                                </div> -->
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
  