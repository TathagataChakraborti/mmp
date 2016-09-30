(define
(domain grounded-FETCHWORLD)
(:requirements :strips :action-costs)

(:predicates
( HOLDING_B1 )
( HAND-TUCKED )
( NOT-HAND-TUCKED )
( BLOCK-AT_B1_LOC2 )
( BLOCK-AT_B1_LOC1 )
( ROBOT-AT_LOC2 )
( HAND-EMPTY )
( ROBOT-AT_LOC1 )
)

(:action TUCK
:parameters ()
:precondition
(and
( NOT-HAND-TUCKED )
)
:effect
(and
( HAND-TUCKED )
(not ( NOT-HAND-TUCKED ))
)
)

(:action MOVE_LOC2_LOC1
:parameters ()
:precondition
(and
( ROBOT-AT_LOC2 )
)
:effect
(and
( ROBOT-AT_LOC1 )
(not ( ROBOT-AT_LOC2 ))
)
)

(:action PICKUP_B1_LOC2
:parameters ()
:precondition
(and
( HAND-EMPTY )
( ROBOT-AT_LOC2 )
( BLOCK-AT_B1_LOC2 )
)
:effect
(and
( HOLDING_B1 )
( NOT-HAND-TUCKED )
(not ( HAND-EMPTY ))
(not ( HAND-TUCKED ))
(not ( BLOCK-AT_B1_LOC2 ))
)
)

(:action PICKUP_B1_LOC1
:parameters ()
:precondition
(and
( HAND-EMPTY )
( BLOCK-AT_B1_LOC1 )
( ROBOT-AT_LOC1 )
)
:effect
(and
( NOT-HAND-TUCKED )
( HOLDING_B1 )
(not ( HAND-TUCKED ))
(not ( HAND-EMPTY ))
(not ( BLOCK-AT_B1_LOC1 ))
)
)

(:action MOVE_LOC1_LOC2
:parameters ()
:precondition
(and
( HAND-TUCKED )
( ROBOT-AT_LOC1 )
)
:effect
(and
( ROBOT-AT_LOC2 )
(not ( ROBOT-AT_LOC1 ))
)
)

(:action PUTDOWN_B1_LOC1
:parameters ()
:precondition
(and
( ROBOT-AT_LOC1 )
( HOLDING_B1 )
)
:effect
(and
( BLOCK-AT_B1_LOC1 )
( NOT-HAND-TUCKED )
( HAND-EMPTY )
(not ( HAND-TUCKED ))
(not ( HOLDING_B1 ))
)
)

(:action PUTDOWN_B1_LOC2
:parameters ()
:precondition
(and
( HOLDING_B1 )
( ROBOT-AT_LOC2 )
)
:effect
(and
( BLOCK-AT_B1_LOC2 )
( NOT-HAND-TUCKED )
( HAND-EMPTY )
(not ( HAND-TUCKED ))
(not ( HOLDING_B1 ))
)
)


)