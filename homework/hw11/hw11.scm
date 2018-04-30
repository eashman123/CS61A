(define (find s predicate)
	(cond
	((null? s) #f)
	((predicate (car s)) (car s)) 
	(else (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
)

(define (has-cycle s)
	(define (cycle-compare s s_rest)
		(cond
		((or (null? (cdr-stream s_rest)) (null? s_rest)) #f)
		((eq? s s_rest) #t)
		(else (cycle-compare (cdr-stream s) (cdr-stream (cdr-stream s_rest)))))
	)
	(cycle-compare s (cdr-stream s))
)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
