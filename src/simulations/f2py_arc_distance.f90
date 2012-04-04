
subroutine arc_distance(aRows, aColumns, a, bRows, bColumns, b, distance_matrix)
  implicit none

  integer, intent(in) :: aRows, aColumns
  double precision, dimension(aRows, aColumns), intent(in) :: a
  integer, intent(in) :: bRows, bColumns
  double precision, dimension(bRows, bColumns), intent(in) :: b

  double precision, dimension(aRows, bRows), intent(out) :: distance_matrix

  double precision ::  temp, theta_1, phi_1, theta_2, phi_2
  integer :: i, j

  do i=1, aRows
     theta_1 = a(i, 1)
     phi_1 = a(i, 1)
     do j=1, bRows
        theta_2 = b(j, 1)
        phi_2 = b(j, 1)
        temp = sin((theta_2-theta_1)/2)**2+cos(theta_1)*cos(theta_2) &
             & *sin((phi_2-phi_1)/2.0d0)**2
        distance_matrix(i, j) =  2.0d0*(atan2(sqrt(temp), sqrt(1.0d0-temp)))
     end do
  end do
end subroutine arc_distance
