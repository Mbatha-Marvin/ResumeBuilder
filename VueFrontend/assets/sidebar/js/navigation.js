export const getNavLinks = () => {
    return [
      {
        title: "Dashboard",
        iconClass: "bi bi-columns-gap",
        to: "/resume/start",
        pathsToMakeActive: ["/resume/start"]
      },
      {
        title: "Profile",
        iconClass: "bi bi-person",
        to: "/resume/profile",
        pathsToMakeActive: ["/resume/profile", "/resume/profile/create"]
      },
      {
        title: "Education",
        iconClass: "bi bi-book",
        to: "/resume/education",
        pathsToMakeActive: ["/resume/education", "/resume/education/create"]
      },
      {
        title: "Experience",
        iconClass: "bi bi-list-stars",
        to: "/resume/experience",
        pathsToMakeActive: ["/resume/experience", "/resume/experience/create"]
      },
      {
        title: "Languages",
        iconClass: "bi bi-translate",
        to: "/resume/language",
        pathsToMakeActive: ["/resume/language", "/resume/language/create"]
      },
      {
        title: "Certification",
        iconClass: "bi bi-patch-check",
        to: "/resume/certification",
        pathsToMakeActive: ["/resume/certification", "/resume/certification/create"]
      },
      {
        title: "Projects",
        iconClass: "bi bi-blockquote-left",
        to: "/resume/project",
        pathsToMakeActive: ["/resume/project", "/resume/project/create"]
      },
      {
        title: "Referees",
        iconClass: "bi bi-sliders2",
        to: "/resume/referee",
        pathsToMakeActive: ["/resume/referee", "/resume/referee/create"]
      },
      {
        title: "Preview",
        iconClass: "bi bi-eye-fill",
        to: "/resume/preview",
        pathsToMakeActive: ["/resume/preview"]
      }
    ];
  };
  