# Waldo Photos Engineering Project



The goal of this project is to produce a working system that can be used
as a conversation piece during your on-site interview. Be prepared to:



* Present your solution to a group of smart engineers like yourself.

* Talk about the decisions that went into the creation of your solution. 

* Explain how you see the solution evolving over time. 

* Discuss the runtime characteristics of the system.

* Discuss technical design tradeoffs and the cost-benefit analysis of
  those decisions.



### Deliverable



Using any language and data-store of your choice, write a console
application that takes two arguments. The arguments are locations of two
image files.



Example:

```bash

subimage ./images/image1.jpeg ./images/image2.jpeg 

```



The application should return information if one of the images is a
cropped part of the other one. If yes, the application should also
return the position of top-left

corner of the cropped image within the original image.



Notes:

 - The images may be provided in any order (the cropped image may be the
   first or the second).

 - The application should work well on JPEGs with some lossy compression
   enabled.



You can make any additional assumptions, as long as you are explicit
about these. 



Please deliver the finished project in a publicly available repository
on Github. Please title the repository as `waldo-${ github-handle }`.



### Evaluation



The main areas we will be evaluating are:



- organization of responsibility

- performance

- resilience to failures.
