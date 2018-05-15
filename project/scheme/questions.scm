(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (cons-all first rests)
  (cond
    ((null? rests) nil)
    (else 
      (cons 
        (append (list first) (car rests))
        (cons-all first (cdr rests))
      )
    )
  )
) ; end of cons-all function

(define (zip pairs)
  ; Gets the first values of all the inner lists
  (define (do-zip s)
    (if (or (null? s) (null? (car s)))
      nil
      (cons 
        (car (car s))
        (do-zip (cdr s))
      )
    ) 
  ) ; end of do-zip function

  ; Gets rest of all the inner lists
  (define (copy lst)
    (if (or (null? lst) (null? (cdr (car lst))))
      nil
      (cons 
        (cdr (car lst))
        (copy (cdr lst))
      )
    )  
  ) ; end of copy function

  ; Applies zip on first elements and rests of inner lists
  (define (apply-zip vals)
    (if (null? vals)
      nil
      (cons 
        (do-zip vals)
        (apply-zip (copy vals))
      )
    )
  ) ; end of apply-zip

  (if (null? pairs)
    (list nil nil)
    (apply-zip pairs)
  )
) ; end of zip function
    
;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (pair-with-index i s)
    (if (null? s) 
      nil
      (cons 
        (list i (car s))
        (pair-with-index (+ 1 i) (cdr s))
      )
    )
  ) ; end of pair-with-index function

  (pair-with-index 0 s)
) ; end of enumerate function
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond
    ((< total 0) 
      nil)
    ((null? denoms) 
      nil)
    ((= total (car denoms))
      (cons 
        (list (car denoms))
        (list-change total (cdr denoms)))
      )
    ((< total (car denoms))
      (list-change total (cdr denoms)))
    (else 
      (append 
        (cons-all 
          (car denoms) 
          (list-change (- total (car denoms)) denoms)
        )
        (list-change total (cdr denoms))
      )
    )
  )

) ; end of list-change function
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
            ; BEGIN PROBLEM 19
            (define form (let-to-lambda form) )
            (cons 
              form
              (cons 
                params 
                (cons 
                  (car (map let-to-lambda body)) 
                  (cdr (map let-to-lambda body))
                ) 
              )
            )
            ; END PROBLEM 19 
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (define zipped (zip values))
           (define vars (map let-to-lambda zipped) )
           (define procedure (car (let-to-lambda body)) )
           (define type-fn (let-to-lambda 'lambda) )

           (cons
            (list type-fn (car vars) procedure)
            (let-to-lambda (car (cdr vars)))
           )
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
