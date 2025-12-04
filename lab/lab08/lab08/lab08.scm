(define (over-or-under num1 num2) 
  (cond
      ((> num1 num2) 1)
      ((= num1 num2) 0)
      (else -1))
)

(define (make-adder num) 
  (lambda (x) (+ x num))
)

(define (composed f g) 
  (lambda (x) (f (g x)))
)

(define (repeat f n)
  (define (helper g k)
    (if (= k 1) 
        g
        (helper (composed f g) (- k 1))    
    )
  )
  (helper f n)
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (define m (max a b))
  (define n (min a b))
  (if (= n 0)
    m
    (gcd n (modulo m n))
  )
)
