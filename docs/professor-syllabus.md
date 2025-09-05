---
layout: page
title: "Professor's Syllabus"
permalink: /professor-syllabus/
---

<!-- This page automatically displays the professor's README.md from the submodule -->
<!-- Any updates the professor makes will appear here automatically -->

{% capture readme_content %}
{% include_relative slides/lecture/README.md %}
{% endcapture %}

<!-- Process the content to fix relative links -->
{% assign processed_content = readme_content 
  | replace: 'lectures/lecture_1/', '/course-materials/lectures/lecture_1/'
  | replace: 'lectures/lecture_2/', '/course-materials/lectures/lecture_2/'
  | replace: 'lectures/lecture_3/', '/course-materials/lectures/lecture_3/'
  | replace: 'lectures/lecture_4/', '/course-materials/lectures/lecture_4/'
  | replace: 'lectures/lecture_5/', '/course-materials/lectures/lecture_5/'
  | replace: 'lectures/lecture_6/', '/course-materials/lectures/lecture_6/'
  | replace: 'lectures/lecture_7/', '/course-materials/lectures/lecture_7/'
  | replace: 'lectures/lecture_8/', '/course-materials/lectures/lecture_8/'
  | replace: 'lectures/lecture_9/', '/course-materials/lectures/lecture_9/'
  | replace: 'lectures/lecture_10/', '/course-materials/lectures/lecture_10/'
  | replace: 'lectures/lecture_13/', '/course-materials/lectures/lecture_13/'
  | replace: 'capstone_project/', '/course-materials/lectures/capstone_project/'
%}

{{ processed_content | markdownify }}