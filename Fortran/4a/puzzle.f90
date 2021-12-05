program puzzle
    implicit none 

    integer :: unit
    character(len=*), parameter :: file_name = 'input.txt'
    integer, parameter :: Nthrows = 100, N = 5
    integer :: throws(Nthrows)
    integer :: Nboards
    integer, allocatable :: boards( :, :, : )
    logical, allocatable :: boards_mark( :, :, : ), rows( :,:), columns( :, :), winners( : )
    integer :: i, iwinner, err 

    open( newunit = unit, file = file_name, action='read', status='old')
    read( unit = unit, fmt = *) throws
    Nboards = 0
    do 
        do i = 1, N
            read(unit = unit, fmt = *, iostat = err )
            if( err > 0) exit
        end do 
        if(err > 0) exit
        read(unit = unit, fmt = * )
        Nboards = Nboards + 1
    end do 
    rewind(unit = unit)

    allocate( boards( Nboards, N, N ) )
    allocate( boards_mark( Nboards, N, N ), rows(Nboards,N), columns(Nboards,N), winners(Nboards) )

    read(unit = unit, fmt=*)
 
    do i = 1, Nboards
        read( unit = unit, fmt = * )
        boards( i, :, : ) = read_board( unit = unit )
    end do 
    close( unit = unit )

    boards_mark = .false.
    rows = .false.
    columns = .false.
    winners = .false.

    do i = 1, Nthrows
        where ( boards == throws(i) ) boards_mark = .true. 
        rows = all( boards_mark, dim=3)
        columns = all( boards_mark, dim=2)
        winners = any( rows .or. columns, dim = 2  )
        if ( any(winners) ) exit 
    end do 

    iwinner = findloc(winners, .true., dim=1)
    
    call print_board(boards(iwinner,:,:))
    print*, ""
    print*, throws(i)*sum(boards(iwinner,:,:), mask = boards_mark(iwinner,:,:) .eqv. .false. )

contains

    function read_board(unit) result(board)
        integer, intent(in) :: unit 
        integer :: i 
        real :: board(N,N)

        do i = 1, N
            read(unit = unit, fmt = * ) board(i,:)
        end do 
    end function
    
    subroutine print_board(board)
        integer, intent(in) :: board( N, N)
        integer :: i 
        do i = 1, N 
            print*, board(i,:)
        end do
    end subroutine    

end program 