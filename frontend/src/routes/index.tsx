import { createBrowserRouter } from 'react-router-dom';
import AppLayout from '../layouts/AppLayout';
import DashboardPage from '../pages/DashboardPage';
import MessagesPage from '../pages/MessagesPage';
import AutomationsPage from '../pages/AutomationsPage';
import AnalyticsPage from '../pages/AnalyticsPage';
import SettingsPage from '../pages/SettingsPage';

const router = createBrowserRouter([
  {
    path: '/',
    element: <AppLayout />,
    children: [
      { index: true, element: <DashboardPage /> },
      { path: 'messages', element: <MessagesPage /> },
      { path: 'automations', element: <AutomationsPage /> },
      { path: 'analytics', element: <AnalyticsPage /> },
      { path: 'settings', element: <SettingsPage /> },
    ],
  },
]);

export default router;
