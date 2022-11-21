
      program weibull

      integer i,kk,cc
      real k,c,bin,pdir,diff,mindiff
      real k_save,c_save
      real u(6),f(6),w(6)

      k = 2.0     ! shape parameter
      c = 6.0     ! scale parameter
C-----      bin = 2.0   ! histogram bin size 
      off = 1.0   ! location or offset value
      pdir = 12.4 ! wind direction probability (%)

      u = (/1.0,3.0,5.0,7.0,9.0,11.0/) ! centre of wind speed bins
      f = (/0.1,2.4,5.7,3.2,0.8,0.2/) ! frequency values

      f = f/pdir ! normalise by pdir

      write(6,'(6(f9.6,1X))') f
       
      mindiff = 1000.0

      do kk = 0,400  ! k=2 (1 -> 5)
      do cc = 0,400  ! c=6 (4 -> 8)

        k = 1.0 + real(kk)/100.0
        c = 4.0 + real(cc)/100.0

        diff = 0
        do i=1,6
          w(i) = (k/c)*(((u(i)-off)/c)**(k-1))*exp(-(((u(i)-off)/c)**k))
          diff = diff + abs(w(i)-f(i))
        enddo

        if (diff.lt.mindiff) then
          mindiff = diff
          k_save = k
          c_save = c
        endif 
      
      enddo
      enddo

      write(6,*)"k_save=",k_save
      write(6,*)"c_save=",c_save

      end

